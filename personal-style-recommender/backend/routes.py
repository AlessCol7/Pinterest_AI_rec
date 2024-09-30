from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import os

scrollnum = 1
sleepTimer = 1

var = "makeup"
url = f"https://www.pinterest.com/search/pins/?q={var}"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Update the driver initialization
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(url)

# Initialize the list to store image URLs
image_data = []

# Scroll down to load more images
for _ in range(scrollnum):
    driver.execute_script("window.scrollTo(1,1000000)")
    print("scroll down")
    time.sleep(sleepTimer)

soup = BeautifulSoup(driver.page_source, 'html.parser')

# Collect image URLs
for link in soup.findAll('img'):
    img_url = link.get('src')
    if img_url:  # Ensure the URL is not None
        image_data.append({'url': img_url})

# Convert the list to a DataFrame and save to CSV
df = pd.DataFrame(image_data)  # Create a DataFrame from the list
df.to_csv('./personal-style-recommender/data/images.csv', index=False)  # Save the DataFrame to a CSV file

# Clean up
time.sleep(30)  # Keeps the browser open for 30 seconds
driver.quit()
