from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import bs4
from bs4 import BeautifulSoup
import time
import random
import os
import requests
import shutil

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
    
]
chrome_options = Options()
chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")

driver_path = r"C:\Users\KAMESH\OneDrive\Desktop\DATA SCIENCE\ASSIGNMENT ANSWERS\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

search_url = 'https://cornerstone.lk/'
driver.get(search_url)
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(3)  


page_html = driver.page_source
pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')


containers = pageSoup.findAll('div', {'class': "col-md-4 mb-4"})
len_containers = len(containers)


if not os.path.exists('images'):
    os.makedirs('images')


def download_image(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)


counter = 1


for container in containers:
    image_element = container.find('img')
    if image_element:
        image_url = image_element['src']
        
        file_path = os.path.join('images', f'image_{counter}.jpg')
        
        download_image(image_url, file_path)
        counter += 1  

print("Images have been downloaded and saved to the 'images' directory.")


shutil.make_archive('images', 'zip', 'images')
print("Images have been zipped into 'images.zip'.")


driver.quit()
