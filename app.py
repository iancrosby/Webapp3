import os
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_update_planet')
def get_planet():
	"""gets the latest location from the client"""
	global location
	location = request.args.get('planet')
	return jsonify(planet=location + " success!")

@app.route('/_send_planet_data')
def send_planet_data():
	"""sends planet data to the client"""
	planet_data = planet_dict[location].p_data
	return jsonify(planet_data=planet_data)


class planet:
	'''This is a planet. It has a location and data.'''
	def __init__(self, x=0, y=0, p_data="No data yet"):
		
		self.x = x
		self.y = y
		self.p_data = p_data
		
	def update_coord(self, x, y):
		
		self.x = x
		self.y = y
		
	def update_data(self, p_data):
	
		self.p_data = p_data

# set up some initial planets
planet1 = planet(40, 80, "The first planet")
planet2 = planet(80, 100, "The second planet")
planet3 = planet(120, 160, "The third planet")
planet4 = planet(70, 40, "The fourth planet")
planet_dict = {'planet1' : planet1, 'planet2' : planet2, 'planet3' : planet3, 'planet4' : planet4}

location = "planet1"







if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
