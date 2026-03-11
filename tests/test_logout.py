import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver
from data import Credentials

# Выход из учетной записи
def test_logout(logged_in_driver):
    
    logged_in_driver.find_element(*Locators.personal_account_button).click()
    WebDriverWait(logged_in_driver, 6).until(EC.visibility_of_element_located(Locators.profile))
    logged_in_driver.find_element(*Locators.logout_button).click()
    WebDriverWait(logged_in_driver, 6).until(EC.visibility_of_element_located(Locators.login_button))
    assert logged_in_driver.find_element(*Locators.login_button).is_displayed()