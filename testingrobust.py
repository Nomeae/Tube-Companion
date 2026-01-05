import requests
from rich import print
#all functions are defined below
def keyConfig():
    key = ""
    key = input("Enter your personal TFL Unified API key (if you have none leave this blank)")
    if key == "":
        key = 'd417c07a1df045af8cb5c17bdf9e783f'
    return key


def stationNaptan():
    station = ""
    while station == "":
        station = input("Enter a station: ").lower()
        station = station.replace("and", "%20")
        station = station.replace("&","%20")
        station = station.replace(" ", "%20")
        station = station.replace("-", "%20")
        station = station.strip()
        stationcheck = requests.get(f"https://api.tfl.gov.uk/StopPoint/Search/{station}")
        jsondata = stationcheck.json() #actual json recieve
        stationcheck = jsondata['total']
        if stationcheck == 0:
            print("Please enter a valid station, did you spell it correctly?")
            station = ""
        else:
            matches = [
                m for m in jsondata.get("matches", [])
                if "tube" in m.get("modes", [])
            ]
            naptancode=matches[0]["id"]
            return naptancode

def lineStatus():
    while line == ():
        valid_lines = ["bakerloo", "northern", "piccadilly", "central", "circle", "district", "hammersmith-city",
                       "jubilee", "metropolitan", "victoria", "waterloo-city"]
        print("Type 'help' if you want a list of lines.")
        line = input("Enter a line: ").lower()
        while "  " in line and "and" not in line and "&" not in line:
            line = line.replace("  ", " ") #boredom aero made this btw
        line = line.replace("and", "-")
        line = line.replace("&", "-")
        line = line.replace(" ", "") #boredom aero
        line = line.strip()
        if line not in valid_lines and line != ("help"):
            print("Please enter a valid line")
            line = () #end of input checking
        elif line == ("help"):
            for i in valid_lines:
                print(i.capitalize())
                line = ()
    line_get = requests.get(f"https://api.tfl.gov.uk/Line/{line}/Status?app_key={key}") #make initial request
    jsondata = line_get.json() #actual array (ty boredom)
    arrayread = jsondata[0] #first thingy in array
    status = arrayread['lineStatuses'][0]['statusSeverityDescription'].upper()
    line = line.replace("-"," AND ").upper()
    print(status, f"On the {line} line")
naptancode = (stationNaptan())
print(naptancode)









