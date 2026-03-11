import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver

# Переход по клику на «Личный кабинет»
def test_personal_account_button(logged_in_driver):

    logged_in_driver.find_element(*Locators.personal_account_button).click()
    WebDriverWait(logged_in_driver, 6).until(EC.visibility_of_element_located(Locators.profile))
    assert logged_in_driver.find_element(*Locators.order_history).is_displayed()