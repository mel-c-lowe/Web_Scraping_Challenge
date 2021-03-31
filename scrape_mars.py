# Dependencies
import pandas as pd
from bs4 import BeautifulSoup as BS
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

# Set up empty dictionary to fill with data from scrape functions
mars_data = {}


def scrape_news():

    # Initialize browser
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Portion of function for news title and teaser copy

    news_url = ("https://redplanetscience.com/#")
    browser.visit(news_url)
    html = browser.html
    soup = BS(html, 'html.parser')

    # Retrieve the title and news teaser
    news_title = soup.find('div', class_='content_title').text
    article_teaser = soup.find('div', class_='article_teaser_body').text

    mars_data["news_title"] = news_title
    mars_data["article_teaser"] = article_teaser

    return mars_data
    
    browser.quit()

def scrape_jpl():

    # Initialize browser
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Portion of function for JPL images

    jpl_url = ("https://spaceimages-mars.com/")
    browser.visit(jpl_url)
    html = browser.html
    soup = BS(html, 'html.parser')

    # Retrieve featured image url
    response = soup.find('a', class_='showimg')
    href = response['href']
    img_url = jpl_url + href

    mars_data["featured_img"] = img_url

    return mars_data

    browser.quit()

image_urls = []

def scrape_hemispheres():

    # Initialize browser
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Portion of function for hemisphere images

    hemisphere_url = 'https://marshemispheres.com/'
    browser.visit(hemisphere_url)
    html = browser.html
    soup = BS(html, 'html.parser')

    images = soup.find_all('div', class_='item')

    for image in images:

        # Grab link of first image to tell browser to move to
        partial_img_url = image.find('a', class_='itemLink product-item')['href']

        # Visit link of full image
        browser.visit(hemisphere_url + partial_img_url)

        # Set up html object for newly visited page
        partial_img_html = browser.html

        # Parse the new page with beautifulsoup
        soup = BS(partial_img_html, 'html.parser')
        
        # Retrieve the full size image source
        img_url = hemisphere_url + soup.find('img', class_='wide-image')['src']

        # Pull title of image
        title = soup.find('h2', class_='title').text

        # Append new values to list of dictionaries
        image_urls.append({"title": title, "img_url": img_url})

        mars_data["hemisphere_img_urls"] = image_urls

    return mars_data

    browser.quit()

def scrape_table():

    # Initialize browser
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Portion of function for Mars facts

    facts_url = 'https://galaxyfacts-mars.com/'
    browser.visit(facts_url)
    html = browser.html
    soup = BS(html, 'html.parser')

    # Pull all the tables on the page
    tables = pd.read_html(facts_url)

    # Isolate the desired table
    mars_facts = tables[0]

    # Clean up header and index
    mars_facts.columns = mars_facts.iloc[0]
    mars_facts = mars_facts.drop(mars_facts.index[0])
    mars_facts.set_index('Mars - Earth Comparison', inplace=True)

    # Convert to html table string
    mars_html = mars_facts.to_html('mars_facts.html')

    # Add to database
    # This is not adding to my database and I don't know why
    mars_data["mars_facts"] = mars_html

    return mars_data

    browser.quit()