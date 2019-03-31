#################################################
# MongoDB and Flask Application
#################################################

# Dependencies and Setup
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# PyMongo Connection Setup
#################################################
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#################################################
# Flask Routes
#################################################
# Root Route to Query MongoDB & Pass Mars Data Into HTML Template to Display the Data
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)