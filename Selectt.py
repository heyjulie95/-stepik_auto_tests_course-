from selenium.webdriver.support.ui import Select
from selenium import webdriver
import math
import time

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects1.html'


try:
    browser = driver
    browser.get(link)
    x = browser.find_element_by_css_selector('span#num1').text
    y = browser.find_element_by_css_selector('span#num2').text
    select = Select(browser.find_element_by_class_name('custom-select'))
    select.select_by_value(f"{int(x) + int(y)}")
    button = browser.find_element_by_css_selector("button.btn-default")
    button.click()
finally:
    time.sleep(3)
    browser.quit()