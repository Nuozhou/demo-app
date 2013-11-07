from flask import Flask, render_template, send_from_directory
from flask.ext.pymongo import PyMongo

import random

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def main():
  # return render_template('static/index.html')
  return send_from_directory('static', 'index.html')

@app.route('/api')
def home_page():
  mongo.db.users.save({"name": "Waseem", "random": random.random()})
  # users = mongo.db.users.find()
  # app.logger.debug("Found user")
  # app.logger.debug(users.size())
  return "Hello World!%s %d" % (app.name, mongo.db.users.count())

@app.route('/<path:filename>')
def send_pic(filename):
  return send_from_directory('/static', filename)

if __name__ == "__main__":
  app.debug = True
  app.run()