# Winter Hacklymptics
# DonationStation

### By: Kyle Java, Neala Mendoza, Anish Dhandore

## Inspiration
We wanted to build a platform in order to help the homeless population in a user’s community. Thrift stores were created to help sell secondhand clothes and materials at reasonable prices and to help fund charitable places. We thought it would be a great idea to find new ways to give back and help the local community.

## What it does
The user will enter the website and have the ability to type in their location or have the website retrieve the location for them. The website is able to get the location of the user via the user's IP address using Radar.io IP geocode. The website will use the user's location and find local thrift stores in that area. The user will then be shown a screen with the names of the thrift stores in that particular area. The webpage will also ask the user if they wanted to see a map view of those thrift stores where it will take the user to another webpage integrated with the Google Map API displaying the locations of those thrift stores.


## How we built it
The frontend was built using HTML, CSS, Bootstrap. The backend was built Radar.io, Google Maps, Python, and Flask. We used Radar.io IP geocode to get the user's location without having the user enter their information. We were also able to search up thrift stores in the user's location with Radar.io places lookup. Radar.io also gave us the coordinates of those stores so, we also took different thrift stores' coordinates to plot it onto the Google Maps.

## Challenges we ran into
It was the first time our team has done a project using Radar.io. The majority of our time was spent learning and reading documentation on how Radar.io works and how to implement it into our project. There was difficulty with reading and understanding the documentation provided for us and lack of examples were available to help us use it.

It was also the first time any of us had used the Google Maps API, so we took some time trying to implement into our website. It was also a challenge trying to pass data from Radar.io to the Google Maps API, in order to show the locations of the stores. Since it was our first time, we did not know how to show the address when a user clicked on a point on the Google Maps API. Initially, we wanted the Google Maps to be smaller, in order to fit more stuff on that webpage, but we were unable to resize it.

Because we spent two days trying to figure out Radar.io and Google Maps we were unable to create the Front-end to the best of our ability. Initially, we wanted multiple webpages, each with their own types of functions and information, but in the end we were only able to get three webpages done.


## Accomplishments that we're proud of
Since this was our first time using Radar.io and the Google Maps API, it was a success being able to implement those. We were proud that we were able to get the user's location with Radar.io as well as find thrift stores in that area with Radar.io. We were also proud that we were able to plot those points on the Google Maps API.

## What we learned
How to use Radar.io, the Google Maps API, and figure out how to integrate those two in our website.

## What's next for DonationStation
Cleaning up the Front-End of the website. Making the map smaller and having the ability to view the addresses when a marker is clicked on in the Google Maps. Implement more webpages with various functionalities. Also, a webpage to show more information about that particular thrift store, like the hours, rating, and etc.
