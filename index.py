
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import urllib
from selenium.webdriver import DesiredCapabilities


def start_driver(): 
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-extensions')  
    options.add_argument('--start-maximized')   
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')  
    options.add_argument('--disable-dev-shm-usage') 


    try:
        driver_path = ChromeDriverManager().install()
        service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service, options=options)

    except ValueError:
        latest_chromedriver_version_url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
        latest_chromedriver_version = urllib.request.urlopen(latest_chromedriver_version_url).read().decode('utf-8')
        service = Service(ChromeDriverManager(driver_version=latest_chromedriver_version).install())

        driver = webdriver.Chrome(service=service, options=options)

    wait = WebDriverWait(driver, 10000)

    return driver

start_driver()