import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver


# Переход из раздела "Булки" в раздел "Начинки"
def test_navigate_buns_to_fillings(logged_in_driver):

    logged_in_driver.find_element(*Locators.fillings_section).click()
    assert logged_in_driver.find_element(*Locators.selected_section).text == "Начинки"

# Переход из раздела "Начинки" в раздел "Соусы"
def test_navigate_fillings_to_sauses(logged_in_driver):
    
    logged_in_driver.find_element(*Locators.fillings_section).click()
    logged_in_driver.find_element(*Locators.sauces_section).click()
    assert logged_in_driver.find_element(*Locators.selected_section).text == "Соусы"


# Переход из раздела "Соусы" в раздел "Булки"
def test_navigate_sausec_to_buns(logged_in_driver):
    
    logged_in_driver.find_element(*Locators.sauces_section).click()
    WebDriverWait(logged_in_driver, 6).until(EC.visibility_of_element_located(Locators.selected_section))
    logged_in_driver.find_element(*Locators.buns_section).click()
    assert logged_in_driver.find_element(*Locators.selected_section).text == "Булки"