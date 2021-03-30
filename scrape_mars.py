# Dependencies
from bs4 import BeautifulSoup as BS
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape_news():

    # Initialize browser

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_data = {}

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

    print(mars_data)
