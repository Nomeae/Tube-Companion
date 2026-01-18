import json
import requests
import re
from fuzzywuzzy import process
from config import KEY

def stationArrivals(station, line):
    with open("atcos.json", "r", encoding="utf-8") as f:
        stations = json.load(f)
    common_names = [s["station_name"] for s in stations]
    closest_station, score = process.extractOne(station, common_names)
    matching_stations = [
        s for s in stations
        if s["station_name"] == closest_station and s["line_id"] == line.lower()
    ]
    atco = matching_stations[0]["station_id"] if matching_stations else None
    if not atco:
        return []
    arrival_get = requests.get(f"https://api.tfl.gov.uk/Line/{line}/Arrivals/{atco}?app_key={KEY}")
    if arrival_get.status_code != 200:
        return []
    arrival_data = []
    for arrival in arrival_get.json():
        platform = arrival["platformName"]
        time_seconds = arrival["timeToStation"]
        destination = arrival["towards"]
        time_minutes = time_seconds // 60
        arrival_data.append({
            "platform": platform,
            "destination": destination,
            "time_minutes": time_minutes
        })
    def platform_number(text):
        match = re.search(r"\d+", text)
        return int(match.group()) if match else 0
    arrival_data.sort(key=lambda x: (platform_number(x["platform"]), x["time_minutes"]))
    for a in arrival_data:
        if a["time_minutes"] == 0:
            a["time_minutes"] = "[rgb(82,255,108)]Due[/]"
    return arrival_data












