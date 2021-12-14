from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

mongo = PyMongo(app)


@app.route('/')
def home():
    mars_data = mongo.db.collection.find_one()
    return render_template("index.html, mars=mars_data")


@app.route('/scrape')
def mars_scrape():
    info_mars = scrape_mars.scrape_info()
    mongo.db.collection.update({}, info_mars, upsert=True)
    return redirect(url_for('home'))


if__name__ == "__main__"
    app.run(debug=True)
