from flask import Flask, render_template, request, redirect
from search import *
from map import *
from keys import *
app = Flask(__name__)

@app.route('/')
def index():
    if (request.method == 'POST'):
        return redirect(url_for('results'))
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    coordinates = {}
    if (request.method == 'POST'):
        getMap()
        coordinates = getUserLocationAutomatically()

    return render_template('search.html' , coordinates = coordinates)

@app.route('/map', methods=['GET', 'POST'])
def map():
    coordinates = getUserLocationAutomatically()
    print(coordinates)
    data = findStoresInLocation(coordinates)
    print(data)
    lat = getLat(data)
    lng = getLng(data)
    getMap(lat , lng , coordinates['lon'], coordinates['lat'])
    return render_template('map.html')


@app.route('/results' ,methods=['GET', 'POST'])
def results():
    coordinates = getUserLocationAutomatically()
    user_city = getCityFromCoordinates(coordinates)
    places = findStoresInLocation(coordinates)
    return render_template('results.html' , user_city = user_city , places = places)

if __name__=="__main__":
    app.run(debug=True)
