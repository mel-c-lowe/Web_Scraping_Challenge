# Dependencies
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