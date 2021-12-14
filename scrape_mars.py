# Import Dependecies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import requests
import pymongo

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_news_db
collection = db.articles


def scraper():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    browser.quit()

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    img_url = "https://spaceimages-mars.com"
    browser.visit(img_url)

    img_html = browser.html
    soup = bs(img_html, "html.parser")

    img_tag = browser.find_by_tag('button')[1].click()
    img = browser.find_by_css('img.fancybox-image')['src']

    browser.quit()

    mars_facts = pd.read_html('https://galaxyfacts-mars.com/',
                              index_col=0, header=0)[0].to_html(classes='table table-striped')

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    hemi_url = ('https://marshemispheres.com/')

    hemispheres = []

    for i in range(4):
        hemisphere = {}
        browser.find_by_css('a.itemLink h3')[i].click()
        hemisphere['title'] = browser.find_by_tag('h2').text
        hemisphere['url'] = browser.find_by_text('Sample')['href']
        hemispheres.append(hemisphere)
        browser.back()
    browser.quit()

    mars_web_info = {
        'Mars News': news_title,
        'Mars Paragraph': news_p,
        'Featured Image': img,
        'Mars Facts': mars_facts,
        'Hemispheres': hemispheres
    }
    return mars_web_info
