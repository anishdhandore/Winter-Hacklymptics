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
    return (data['places'])


def createGeofence(places):
    url = 'https://api.radar.io/v1/geofences'
    for place in places:
        #url = ('https://api.radar.io/v1/geofences'+'\description='+place['name'] +"\type=" + place['location']['type']+ '\coordinates=' + str(place['location']['coordinates']))
        req = requests.post(url = url , headers = HEADERS)
        print(req)

coordinates= getUserLocationAutomatically()
data = findStoresInLocation(coordinates)

tag = '123test'
externalId = 'extest'
description = 'myshop'
coordinates = [33.4936408996582,-117.14836120605469]
radius = 100
type = 'circle'
url  = 'https://api.radar.io/v1/geofences/thriftstorename/3'
data = requests.put(url  = url , headers = HEADERS)
print(data)


url = 'https://api.radar.io/v1/geofences'
data = requests.get(url = url, headers= HEADERS)
data = data.json()
pprint(data)
