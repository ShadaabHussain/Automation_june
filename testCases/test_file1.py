import time
import allure
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service

headless_option = webdriver.ChromeOptions()
headless_option.add_argument("headless")


class Test_Pytet:

    @pytest.mark.regression
    def test_sum_001(self):
        a = 4
        b = 3
        sum = a + b
        print(sum)
        if sum == 7:
            assert True
        else:
            assert False

    @pytest.mark.regression
    def test_minus_002(self):
        a = 5
        b = 2
        minus = a - b
        print(minus)
        if minus == 3:
            assert True
        else:
            assert False

    @pytest.mark.regression
    def test_Credence_003(self):
        driver = webdriver.Chrome(options=headless_option)

        driver.get("https://credence.in/")
        driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()
        l = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a"))
        print(l)
        contact_num_list = []

        for r in range(1, l + 1):
            Contact_num = driver.find_element(By.XPATH,
                                              "//div[@class='quickfinder-description gem-text-output']//p//a[" +
                                              str(r) + "]").text
            print(Contact_num)
            contact_num_list.append(Contact_num)
        print(contact_num_list)
        if "+91 8983282704" in contact_num_list:
            print(contact_num_list.index("+91 8983282704"))
            assert True

        else:
            assert False

    @pytest.mark.regression
    def test_Registration_004(self):
        driver = webdriver.Chrome(options=headless_option)

        driver.get("https://automation.credence.in/shop")

        driver.find_element(By.XPATH, '//*[@id="navbar"]/ul[2]/li[4]/a').click()

        driver.find_element(By.ID, "name").send_keys("Test1")

        driver.find_element(By.ID, "email").send_keys("test28@gmail.com")

        driver.find_element(By.ID, "password").send_keys("Vampire@123")

        driver.find_element(By.ID, "password-confirm").send_keys("Vampire@123")

        driver.find_element(By.CLASS_NAME, "btn").click()

        # if driver.title == "CredKart":
        #     print("Registration is completed")
        # else:
        #     print("Registration Failed")

        try:
            driver.find_element(By.XPATH, '/html/body/div/div[1]/h2')
            print("Registration is completed")
        except (NoSuchElementException, TimeoutException):
            print("Registration Failed")

    @pytest.mark.regression
    def test_login_005(self):

        driver = webdriver.Chrome(options=headless_option)

        driver.get("https://automation.credence.in/shop")

        driver.find_element(By.LINK_TEXT, 'Login').click()
        driver.find_element(By.ID, 'email').send_keys('test27@gmail.com')
        driver.find_element(By.ID, 'password').send_keys('Vampire@123')
        driver.find_element(By.CLASS_NAME, 'btn').click()

        driver.find_element(By.XPATH, '//*[@id="navbar"]/ul[2]/li[3]/a').click()
        driver.find_element(By.XPATH, '//*[@id="navbar"]/ul[2]/li[3]/ul/li/a').click()

        time.sleep(5)

        if driver.title == "CredKart":
            print("Login is completed")
        else:
            print("Login Failed")

# pytest -v -n=3 --html=Reports/myreport.html
