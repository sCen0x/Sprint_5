import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    
    email = 'maslennikov_36@gmail.com'
    password = 'qwerty123456'
    
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*Locators.login_button_main_page).click()
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    
    yield driver