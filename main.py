from flask import Flask, render_template, request
from pymongo import MongoClient
import os

mongouser=os.environ['MONGO_USER']
mongopwd=os.environ['MONGO_PWD']
mongohost=os.environ['MONGO_HOST']
app = Flask(__name__)
client = MongoClient('mongodb://%s:%s@%s:27017' % (mongouser, mongopwd, mongohost))

@app.route('/')
def index():
	return retrieve_records()

@app.route('/add', methods=['GET', 'POST'])
def add():
	if request.method == "POST":
		details = request.form
		carName = details['cname']
		carPrice = details['cprice']
		db = client.testdb
		db.cars.insert_one({'name': carName, 'price': carPrice})
		return retrieve_records()
	return render_template('add.html')

def retrieve_records():
	db = client.testdb
	reqs = db.cars.find({}, {'name': 1, 'price': 1}).sort("name")
	return render_template('cars.html', reqs=reqs, content_type='application/json')

if __name__ == '__main__':
	app.run(host= '0.0.0.0', debug=True)
