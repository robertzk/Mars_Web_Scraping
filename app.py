from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_website"
mongo = PyMongo(app)


@app.route("/")
def index():
    mars_website = mongo.db.mars_website.find_one()
    return render_template("index.html", mars_website=mars_website)


@app.route("/scrape")
def scrape():
    mars_mission = mongo.db.mars_website
    mars_website_data = scraper.scrape()
    mars_website.update({}, mars_website_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)