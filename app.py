from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__, template_folder='templates')

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_websites")


@app.route("/")
def index():
    mars_websites = mongo.db.collection.find()
    return render_template("index.html", mars_websites=mars_websites)


@app.route("/scrape")
def scrape():
    # mars_websites = mongo.db.collection.find()
    mars_website_data = scrape_mars.scrape()
    mongo.db.collection.insert_one(mars_website_data)
    # mars_website.insert_one(mars_website_data)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
