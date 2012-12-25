from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello world!'
	
app.run()
