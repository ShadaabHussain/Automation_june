import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
headless_option =webdriver.ChromeOptions()
headless_option.add_argument("headless")

driver = webdriver.Chrome(options=headless_option)

driver.get("https://automation.credence.in/shop")

driver.find_element(By.LINK_TEXT,'Login').click()
driver.find_element(By.ID,'email').send_keys('test21@gmail.com')
driver.find_element(By.ID,'password').send_keys('Vampire@123')
driver.find_element(By.CLASS_NAME,'btn').click()

driver.find_element(By.XPATH,'//*[@id="navbar"]/ul[2]/li[3]/a').click()
driver.find_element(By.XPATH,'//*[@id="navbar"]/ul[2]/li[3]/ul/li/a').click()

time.sleep(5)

if driver.title == "CredKart":
    print("Registration is completed")
else:
    print("Registration Failed")
