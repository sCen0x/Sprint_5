import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver

# Переход по клику на «Конструктор» из личного кабинета
def test_go_to_constructor_from_personal_account_by_constructor_button(logged_in_driver):
    
    logged_in_driver.find_element(*Locators.personal_account_button).click()
    WebDriverWait(logged_in_driver, 6).until(EC.visibility_of_element_located(Locators.profile))
    logged_in_driver.find_element(*Locators.constructor_button_in_header).click()
    WebDriverWait(logged_in_driver, 6).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    assert logged_in_driver.find_element(*Locators.make_an_order_button).is_displayed()

# Переход по клику на логотип Stellar Burgers из личного кабинета
def test_go_to_constructor_from_personal_account_by_logo(logged_in_driver):

    logged_in_driver.find_element(*Locators.personal_account_button).click()
    WebDriverWait(logged_in_driver, 6).until(EC.visibility_of_element_located(Locators.profile))
    logged_in_driver.find_element(*Locators.logo).click()
    WebDriverWait(logged_in_driver, 6).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    assert logged_in_driver.find_element(*Locators.make_an_order_button).is_displayed()