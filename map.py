from keys import *
import gmplot

def getMap(attractions_lats , attractions_lngs , my_lng, my_lat):
    # Create the map plotter:
    apikey = api_key # (your API key here)
    gmap = gmplot.GoogleMapPlotter(33.4936408996582,-117.14836120605469, 14, apikey=apikey)

    # Mark a hidden gem:
    gmap.marker(37.770776, -122.461689, color='cornflowerblue')

    # Highlight some attractions:
    attractions_lats, attractions_lngs = zip(*[
        (33.50803, -117.142051),
        (33.511451, -117.160034),
        (33.508071, -117.124669),
        (33.51651586360942, -117.16274810169405),
        (33.516662, -117.124372),
        (33.475274, -117.16311)
    ])
    gmap.scatter(attractions_lats, attractions_lngs, color='#3B0B39', size=40, marker=True)

    # Outline the Golden Gate Park:



    # Draw the map to an HTML file:
    gmap.draw('templates/map.html')
