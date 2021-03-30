# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars

# Create flask app
app = Flask(__name__)

# Route at index
@app.route("/")
def index():
    return "Hello, Mars!"





if __name__ == "__main__":
    app.run(debug=True)