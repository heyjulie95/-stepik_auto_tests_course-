import selector as selector
from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/math.html'
driver = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = driver
    browser.get(link)

    x_element = browser.find_element_by_css_selector('span#input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_tag_name('input#answer')
    input1.send_keys(f"{y}")
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn-default")
    button.click()capcha.py

finally:
    time.sleep(3)
    browser.quit()
