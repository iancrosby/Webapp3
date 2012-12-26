import os
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@app.route('/')
def index():
    return render_template('index.html')



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

planet = "planet1"

@app.route('/_get_planet')
def get_planet():
	"""gets the latest planet selection from the client"""
	planet = request.args.get('planet', 0, type=str)
	planet = planet & " success!"
	return jsonify(planet)


def send_planet_data():
	"""sends planet data to the client"""
	planet_data = planet_dict[planet].data
	return jsonify(planet_data)


if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
