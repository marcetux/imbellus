Project structure
=================
This project was developed using:

Node.js 8.10
Python 3.6.4
React 16.2.0

.
├── README.md
└── imbellus/
    ├── server/
    └── static/
        ├── css/
        ├── dist/
        ├── images/
        └── js/

Setting up the server
=====================

Install virtual env

virtualenv venv
source venv/bin/activate

Install flask and dependencies

pip3 install Flask
pip3 install requests

Launch the server:

I have added a bootstrap.sh file that can be used to start the server, just run:

    ./boostrap.sh

You can set your key in the server config file located at:

imbellus/server/config.py


Setting up the React App (static)
=================================

I used the NPM package manager to handle my javascript dependencies and I'm using Webpack as my module bundler, I have added a package.json file that will allow you to do an npm install which should take care of the dependencies:

npm install

once the installation finish run:

npm run watch

Now you can visit localhost:5000 to see the frontend portion of the app

Sample API Calls
================

Get geometrical distance

Given the two points (x1, y1) and (x2, y2), the distance d between these points is given by the following:

    radius = 6373 #kilometers

    dlon = destination_lon - origin_lon
    dlat = destination_lat - origin_lat

    a = sin(dlat / 2)**2 + cos(origin_lat) * cos(destination_lat) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = radius * c

Start your server to run the following examples:

Example:
http://localhost:5000/geocode/distance/?origin_lat=40.78&origin_lon=-73.9&destination_lat=42.2&destination_lon=-73.9


Get lat and long
Just a wrapper for the google API

http://localhost:5000/geocode/latlng/200%20n%20san%20fernando%20rd%2090031


Get address
Just a wrapper for the google API

http://localhost:5000/geocode/address/40.71,-73.96


Technical challenges and pending items
======================================

I remember you mentioned this was suppose to take an hour, and  I'm way beyond that time... so I'm submitting this as I have it today for you to assess my progress... or lack of it :/

Here is what is pending:

This application does not implement any sort of caching for the api calls made to google.

The application doesn't consider API limit rates

The UI is not functional, I wish I had more time to work on the UI and learn React better, I intended to use a google map but I ran out of time here..., I end up just logging the API calls to the console...

Flask is nice, but I need to take more time to read on how to properly implement validations, as of now I did not implement validations for the API parameters

The application does not use any logging framework

Test have not been written

I do appreciate the time you took to review this.

Hector M




