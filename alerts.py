import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/alert_accept.html'
driver = webdriver.Chrome()


try:
    browser = driver
    browser.get(link)
    button = browser.find_element_by_css_selector('button')
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(2)
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    field = browser.find_element_by_css_selector('input.form-control')
    field.send_keys(y)
    submit = browser.find_element_by_css_selector('button.btn-primary')
    submit.click()
    time.sleep(3)
finally:
    browser.quit()
