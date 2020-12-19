import requests
import json
from pprint import pprint
from keys import *


def getUserLocationAutomatically():
    coordinates = {
        'lat': '',
        'lon': ''
    }
    url = ' https://api.radar.io/v1/geocode/ip'
    data = requests.get(url = url, headers = HEADERS)
    data = data.json()
    coordinates['lat'] = str(data['address']['latitude'])
    coordinates['lon'] = str(data['address']['longitude'])
    return coordinates


def getUserLocationManually(location):
    url = "https://api.radar.io/v1/geocode/forward?query={}".format(location)
    data = requests.get(url)
    data = data.json()
    #pprint(data)
    latitude = data["addresses"][0]["latitude"]
    longitude = data["addresses"][0]["longitude"]
    return latitude, longitude

def findStoresInLocation(coordinates):
    url ="https://api.radar.io/v1/search/places?categories=thrift-or-consignment-store&near=+"+ coordinates['lat']+ ","+coordinates['lon']+"&radius=10000&limit=10"
    data = requests.get(url = url, headers = HEADERS)
    data = data.json()
    pprint(data)
