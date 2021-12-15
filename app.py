from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__, template_folder='templates')

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_website")


@app.route("/")
def index():
    mars_websites = mongo.db.mars_website.find({})
    mars_websites = { key.replace(" ", "_").lower(): value for (key, value) in mars_websites.items() }
    return render_template("index.html", mars_websites=list(mars_websites))


@app.route("/scrape")
def scrape():
    # mars_websites = mongo.db.collection.find()
    mars_website_data = scrape_mars.scrape()
    mongo.db.mars_website.insert_one(mars_website_data)
    # mars_website.insert_one(mars_website_data)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
