from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__, template_folder='templates')

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_website")

@app.route("/")
def index():
    mars_website = mongo.db.collection.find_one()
    return render_template("index.html", mars_website=mars_website)


@app.route("/scrape")
def scrape():
    mars_website = mongo.db.collection.find_one()
    mars_website_data = scrape_mars.scrape()
    mongo.db.collection.replace_one({}, mars_website, upsert=True)
    # mars_website.insert_one(mars_website_data)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
