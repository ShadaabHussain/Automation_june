import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://automation.credence.in/")
    return driver

