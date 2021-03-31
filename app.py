# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars

# Create flask app
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/app")

# Route at index
@app.route("/")
def index():
    return "Hello, Mars! Let's get data!"

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