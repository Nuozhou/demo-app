from flask import Flask, render_template, send_from_directory, jsonify, request
from flask.ext.pymongo import PyMongo
from bson import BSON, json_util
from bson.json_util import dumps
import json

import random

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def main():
  # return render_template('static/index.html')
  return send_from_directory('static', 'index.html')

@app.route('/api/get/<int:userid>')
def get_all_items(userid):
	# Query mongo db for all todo items
	items = mongo.db.todoitems.find( { "userid" : userid } )

	# Dump the result into json, HTTP 200 OK, set content-type header
	if(items.count() == 0):
		jsondict = []
	else:
		jsondict = items[0]["items"]

	return dumps(jsondict, sort_keys=True, indent=4, default=json_util.default), 200, {"Content-Type" : "application/json"}

@app.route('/api/put/<int:userid>', methods=['POST'])
# accepts POST items={...}
def set_all_items(userid):
	# Get the items from the request into a native list
	items = json.loads(request.form['items'])

	#mongo.db.todoitems.remove( { "userid" : userid } )

	record =  {
			"userid" : userid,
			"items" : items
		}

	#mongo.db.todoitems.save(record)
	mongo.db.todoitems.update( { "userid" : userid }, record, True)

	app.logger.debug(items)
	return "OK", 200, {"Content-Type" : "application/json"}

"""
@app.route('/api')
def home_page():
  mongo.db.users.save({"name": "Waseem", "random": random.random()})
  # users = mongo.db.users.find()
  # app.logger.debug("Found user")
  # app.logger.debug(users.size())
  return "Hello World!%s %d" % (app.name, mongo.db.users.count())
"""

@app.route('/<path:filename>')
def send_pic(filename):
  return send_from_directory('/static', filename)

if __name__ == "__main__":
  app.debug = True
  app.run()