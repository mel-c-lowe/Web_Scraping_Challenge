# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars
import pymongo

# Create flask app
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.app
mars_db = db.mars_db

# Route at index
@app.route("/")
def index():
    # return "Hello, Mars! Let's get data!"

    # listings = mongo.db.listings.find_one()
    mars_stuff = mongo.db.mars_stuff.find_one()

    return render_template("index.html", mars_db=mars_db)

# Testing initial news scrape
@app.route("/scrape")
def scrape_all():

    # Connect to mongodb
    mars_db = mongo.db.mars_db

    # Scrape news
    mars_data = scrape_mars.scrape_news()

    # Testing second scrape function
    mars_data = scrape_mars.scrape_jpl()

    # Scrape hemisphere images
    mars_data = scrape_mars.scrape_hemispheres()

    #Scrape mars_facts table
    mars_data = scrape_mars.scrape_table()

    mars_db.update({}, mars_data, upsert=True)
    
    return redirect("/", code=302)





if __name__ == "__main__":
    app.run(debug=True)