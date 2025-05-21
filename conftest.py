import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from curl import *
from data import Credentials
from locators import Login


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1400,1000")
    browser = webdriver.Chrome(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()


# Авторизация
@pytest.fixture
def authorization(driver):
    driver.get(auth_link)
    driver.find_element(*Login.EMAIL).send_keys(Credentials.EMAIL)
    driver.find_element(*Login.PASSWORD).send_keys(Credentials.PASSWORD)
    driver.find_element(*Login.AUTH_BUTTON).click()
    return driver
