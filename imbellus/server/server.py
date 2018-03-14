from flask import Flask, render_template, jsonify, request
import requests
from math import sin, cos, sqrt, atan2, radians
import config


app = Flask(__name__, static_folder='../static/dist', template_folder='../static')


search_url = config.IMBELLUS_CONFIG['google_endpoint']
    # raise ValueError("geocode endpoint not specified")

key = config.IMBELLUS_CONFIG['key']
    # raise ValueError("Couldn't not find the key value")


@app.route("/geocode/distance/")
def get_geocode_distance():
    radius = 6373 #kilometers

    origin_lat = float(request.args.get('origin_lat'))
    origin_lon = float(request.args.get('origin_lon'))
    destination_lat = float(request.args.get('destination_lat'))
    destination_lon = float(request.args.get('destination_lon'))

    dlon = destination_lon - origin_lon
    dlat = destination_lat - origin_lat

    a = sin(dlat / 2)**2 + cos(origin_lat) * cos(destination_lat) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = radius * c

    return jsonify({'result': distance})


@app.route("/geocode/latlng/<string:query>")
def get_geocode_by_address(query):
    payload = {"key": key, "address": query}
    req=requests.get(search_url, params=payload)
    response = req.json()

    result = response["results"][0]

    geodata = dict()
    geodata['lat'] = result['geometry']['location']['lat']
    geodata['lng'] = result['geometry']['location']['lng']

    return jsonify({'result': geodata})

@app.route("/geocode/address/<string:query>")
def get_geocode_by_lat_lng(query):
    payload = {"key": key, "latlng": query}
    req=requests.get(search_url, params=payload)
    response = req.json()

    result = response["results"][0]

    geodata = dict()
    geodata['address'] = result['formatted_address']
    return jsonify({'result': geodata})


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/about', methods=["GET"])
def about():
     return jsonify({'message': 'This project was made for Imbellus by Hector Miranda'})

#left it here to make a more verbose endpoint
@app.route("/geocode/<string:query>")
def details(query):
    search_payload = {"key": key, "address": query}

    req=requests.get(search_url, params=search_payload)
    response = req.json()

    result = response["results"][0]

    geodata = dict()
    geodata['lat'] = result['geometry']['location']['lat']
    geodata['lng'] = result['geometry']['location']['lng']
    geodata['address'] = result['formatted_address']

    return jsonify({'result': geodata})


if __name__ == '__main__':
    app.run()