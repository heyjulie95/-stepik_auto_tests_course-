import selector as selector
from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/get_attribute.html'
driver = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = driver
    browser.get(link)
    im = browser.find_element_by_css_selector('img#treasure')
    x = im.get_attribute('valuex')
    y = calc(x)
    input1 = browser.find_element_by_tag_name('input#answer')
    input1.send_keys(f"{y}")
    option1 = browser.find_element_by_css_selector("input#robotCheckbox")
    option1.click()
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_radio.click()
    button = browser.find_element_by_css_selector("button.btn-default")
    button.click()
finally:
    time.sleep(3)
    browser.quit()
