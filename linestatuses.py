from config import KEY
import requests
valid_lines = ["bakerloo", "northern", "piccadilly", "central", "circle", "district", "hammersmith-city",
               "jubilee", "metropolitan", "victoria", "waterloo-city"]

def bakerloo():
    line_get = requests.get(f"https://api.tfl.gov.uk/Line/bakerloo/Status?app_key={KEY}")  # make initial request
    jsondata = line_get.json()  # actual array (ty boredom)
    arrayread = jsondata[0]  # first thingy in array
    status = arrayread['lineStatuses'][0]['statusSeverityDescription'].upper()
    return status

def northern():
    line_get = requests.get(f"https://api.tfl.gov.uk/Line/northern/Status?app_key={KEY}")  # make initial request
    jsondata = line_get.json()  # actual array (ty boredom)
    arrayread = jsondata[0]  # first thingy in array
    status = arrayread['lineStatuses'][0]['statusSeverityDescription'].upper()
    return status

def piccadilly():
    line_get = requests.get(f"https://api.tfl.gov.uk/Line/piccadilly/Status?app_key={KEY}")  # make initial request
    jsondata = line_get.json()  # actual array (ty boredom)
    arrayread = jsondata[0]  # first thingy in array
    status = arrayread['lineStatuses'][0]['statusSeverityDescription'].upper()
    return status

def central():
    line_get = requests.get(f"https://api.tfl.gov.uk/Line/central/Status?app_key={KEY}")  # make initial request
    jsondata = line_get.json()  # actual array (ty boredom)
    arrayread = jsondata[0]  # first thingy in array
    status = arrayread['lineStatuses'][0]['statusSeverityDescription'].upper()
    return status

def circle():
    line_get = requests.get(f"https://api.tfl.gov.uk/Line/circle/Status?app_key={KEY}")  # make initial request
    jsondata = line_get.json()  # actual array (ty boredom)
    arrayread = jsondata[0]  # first thingy in array
    status = arrayread['lineStatuses'][0]['statusSeverityDescription'].upper()
    return status

def district():
    line_get = requests.get(f"https://api.tfl.gov.uk/Line/district/Status?app_key={KEY}")  # make initial request
    jsondata = line_get.json()  # actual array (ty boredom)
    arrayread = jsondata[0]  # first thingy in array
    status = arrayread['lineStatuses'][0]['statusSeverityDescription'].upper()
    return status

def hammersmith():
    line_get = requests.get(f"https://api.tfl.gov.uk/Line/hammersmith-city/Status?app_key={KEY}")  # make initial request
    jsondata = line_get.json()  # actual array (ty boredom)
    arrayread = jsondata[0]  # first thingy in array
    status = arrayread['lineStatuses'][0]['statusSeverityDescription'].upper()
    return status

def jubilee():
    line_get = requests.get(f"https://api.tfl.gov.uk/Line/jubilee/Status?app_key={KEY}")  # make initial request
    jsondata = line_get.json()  # actual array (ty boredom)
    arrayread = jsondata[0]  # first thingy in array
    status = arrayread['lineStatuses'][0]['statusSeverityDescription'].upper()
    return status

def metropolitan():
    line_get = requests.get(f"https://api.tfl.gov.uk/Line/metropolitan/Status?app_key={KEY}")  # make initial request
    jsondata = line_get.json()  # actual array (ty boredom)
    arrayread = jsondata[0]  # first thingy in array
    status = arrayread['lineStatuses'][0]['statusSeverityDescription'].upper()
    return status

def victoria():
    line_get = requests.get(f"https://api.tfl.gov.uk/Line/victoria/Status?app_key={KEY}")  # make initial request
    jsondata = line_get.json()  # actual array (ty boredom)
    arrayread = jsondata[0]  # first thingy in array
    status = arrayread['lineStatuses'][0]['statusSeverityDescription'].upper()
    return status

def waterloo():
    line_get = requests.get(f"https://api.tfl.gov.uk/Line/waterloo-city/Status?app_key={KEY}")  # make initial request
    jsondata = line_get.json()  # actual array (ty boredom)
    arrayread = jsondata[0]  # first thingy in array
    status = arrayread['lineStatuses'][0]['statusSeverityDescription'].upper()
    return status

def stationget():
    station_get = requests.get(f"https://api.tfl.gov.uk/line/{line}/arrivals?app_key={KEY}")  # make initial request
    jsondata = station_get.json()  # actual array (ty boredom)
    return