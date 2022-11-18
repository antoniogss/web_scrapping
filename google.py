from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# It removes the message: Chrome is controlled by automated test software in Selenium
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.google.com')

sleep(3) #seconds

element = driver.find_element(By.TAG_NAME, 'input')

element.send_keys('data') # Type "data" 