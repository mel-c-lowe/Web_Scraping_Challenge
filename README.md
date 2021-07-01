# Web_Scraping_Challenge
UMN Data Analytics Bootcamp Homework 12


Tools Used:

* Python
* Jupyter Notebook
* Beautiful Soup
* Pandas
* Splinter
* MongoDB
* Flask
* HTML
* Bootstrap

### Assignment Overview

* Using a Jupyter Notebook, scrape the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text.

* Visit the url for the Featured Space Image site [here](https://spaceimages-mars.com).

* Use Splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

* Visit the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mars's hemispheres.

* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

* Using MongoDB and Flask, create a new HTML page that displays all the information that was scraped.

* Create a scrape function to execute the code in the Jupyter Notebook and returns one Python dictionary of scraped data and store it in a Mongo database.

* Create a main route that will query the Mongo database and pass the Mars data into an HTML template to display the data.

* Create a template HTML file that will take the Mars data and display it all properly.