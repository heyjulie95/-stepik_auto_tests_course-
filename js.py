from selenium.webdriver.support.ui import Select
from selenium import webdriver
import math
import time


driver = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = driver
    browser.get(link)
    x = browser.find_element_by_css_selector('span#input_value').text
    y = calc(x)

    input1 = browser.find_element_by_css_selector('input#answer')
    input1.send_keys(y)
    checkbox = browser.find_element_by_css_selector('input#robotCheckbox')
    checkbox.click()
    radio = browser.find_element_by_css_selector('input#robotsRule')
    radio.click()
    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()
finally:
    time.sleep(3)
    browser.quit()