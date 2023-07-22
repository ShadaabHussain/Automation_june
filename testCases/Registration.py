from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException ,TimeoutException

driver = webdriver.Chrome()

driver.get("https://automation.credence.in/shop")

driver.find_element(By.XPATH,'//*[@id="navbar"]/ul[2]/li[4]/a').click()

driver.find_element(By.ID,"name").send_keys("Test1")

driver.find_element(By.ID,"email").send_keys("test28@gmail.com")

driver.find_element(By.ID,"password").send_keys("Vampire@123")


driver.find_element(By.ID,"password-confirm").send_keys("Vampire@123")

driver.find_element(By.CLASS_NAME, "btn").click()

# if driver.title == "CredKart":
#     print("Registration is completed")
# else:
#     print("Registration Failed")

try:
    driver.find_element(By.XPATH,'/html/body/div/div[1]/h2')
    print("Registration is completed")
except (NoSuchElementException , TimeoutException):
    print("Registration Failed")

driver.close()



