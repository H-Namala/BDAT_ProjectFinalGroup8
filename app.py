from os import name
from flask import Flask, request, render_template, Markup, send_from_directory
from flask.helpers import send_from_directory
from flask_pymongo import PyMongo, pymongo
import pymongo
from bson.json_util import dumps

app = Flask(__name__)



app.config['MONGO_DBNAME'] = "Covid_db"
app.config['MONGO_URI'] = "mongodb+srv://Namala:DkFtXXVnw008r4iT@cluster0.eqj2s.mongodb.net/Covid_db?retryWrites=true&w=majority"
app.config['MONGO_COLLECTION_NAME'] = "Covid_cases"
mongo = PyMongo(app)



@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template ('Templates/base.html')

@app.route('/data', methods = ['POST', 'GET'])
def Data():
    return render_template ('table.html')
 

@app.route('/stats', methods = ['POST', 'GET'])
def Stats():
    return render_template ('stats.html')

@app.route('/cases', methods = ['POST', 'GET'])
def Totalcases():
    return render_template ('cases.html')





if __name__ == '__main__':
    app.run(debug=True)