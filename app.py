from flask import Flask,render_template,jsonify
import json
import requests

app = Flask(__name__)


@app.route('/')
def home():
	cities = ['New York','London','New Delhi','Mumbai','Tokyo']
	update = [1,0,1,0,1]
	weather = []
	
	index=0
	for city in cities:
		params={
		'access_key': '86ffbac9eabd41ecd8ee9d3bbf8f8b31',
		'query':city
		}
		result = requests.get('http://api.weatherstack.com/current', params)
		response = result.json()
		temperature=response['current']['temperature']
		humidity = response['current']['humidity']
		unit = response['request']['unit']
		image=response['current']['weather_icons'][0]
		updateval=update[index]
		weather.append({'city':city,
						'forecast':{
							'temperature':temperature,
							'humidity':humidity,
							'unit':unit,
							'update':str(updateval)
						},
						'img':image})
		index +=1
	return render_template("home.html",weather=weather)
	


	