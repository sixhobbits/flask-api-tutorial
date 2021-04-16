import requests
from flask import Flask, jsonify

app = Flask(__name__)

WEATHER_URL = 'http://api.weatherstack.com/current?access_key=3d5dc76fc109a6ca25c49652c60d4723'
WEATHER_PARAMS = {'query':'Cape Town'}

EXCHANGE_URL = 'https://openexchangerates.org/api/latest.json?app_id=6712bbd024cb4c1898d1c363b92e167a'
EXCHANGE_PARAMS =  {'symbols':'ZAR,EUR,CHF'}

@app.route('/')
def index():
    return "Welcome to my API!" 

@app.route('/get',methods=['GET']) # Add an endpoint to access our API
def get():
    exchange_data = requests.get(EXCHANGE_URL, EXCHANGE_PARAMS)
    weather = requests.get(WEATHER_URL,params=WEATHER_PARAMS)

    return jsonify({
        'usd_rates': exchange_data.json()['rates'],
        'curr_temp': weather.json()['current']['temperature']
    })


if __name__ == '__main__':
    app.run()
