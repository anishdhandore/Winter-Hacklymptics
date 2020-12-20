from flask import Flask, render_template, request, redirect
from search import *
from map import *
from keys import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    coordinates = {}
    if (request.method == 'POST'):
        coordinates = getUserLocationAutomatically()

    return render_template('search.html' , coordinates = coordinates)

@app.route('/map')
def map():
    getMap()
    return render_template('map.html')


if __name__=="__main__":
    app.run(debug=True)
