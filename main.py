# IMPORT NECCESSARY LIB
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.date import now
from utils.scrapper import blizzard_forum_scrapper
import chromedriver_autoinstaller

# CONFIG FOR PRODUCTION ENV
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

#alive()

while True:
    #driver = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    driver = webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()), options=chrome_options)
       
   
    print('Scraping blizzard forum site...........................', now())
    blizzard_forum_scrapper(driver, WebDriverWait, By, EC)

    # Sleep for 10secs then continue
    time.sleep(4)

