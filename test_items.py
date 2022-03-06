import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
 

def test_btn_add_to_basket(browser):
    browser.get(link)
    feedback = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert  feedback > 0 , 'button add to basket not found'
    time.sleep(10) 