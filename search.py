import requests
import json
from pprint import pprint
from keys import *
from map import *


def getCityFromCoordinates(coordinates):
    url = "https://api.radar.io/v1/geocode/reverse?coordinates="+(coordinates['lat']) + ","+(coordinates['lon'])
    data = requests.get(url = url, headers = HEADERS)
    data = data.json()
    city = data['addresses'][0]['city'] + ", "+data['addresses'][0]['country']
    return city

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
    data = requests.get(url, headers = HEADERS)
    data = data.json()
    #pprint(data)
    latitude = data["addresses"][0]["latitude"]
    longitude = data["addresses"][0]["longitude"]
    return latitude, longitude

def findStoresInLocation(coordinates):
    url ="https://api.radar.io/v1/search/places?categories=thrift-or-consignment-store&near=+"+ coordinates['lat']+ ","+coordinates['lon']+"&radius=10000&limit=10"
    data = requests.get(url = url, headers = HEADERS)
    data = data.json()

    return(data['places'])


def getLat(data):
    lat = []
    for place in data:
        lat.append(place['location']['coordinates'][0])
    return lat

def getLng(data):
    lng = []
    for place in data:
        lng.append(place['location']['coordinates'][1])
    return lng

coordinates = getUserLocationAutomatically()
data = findStoresInLocation(coordinates)
print(getLng(data))
