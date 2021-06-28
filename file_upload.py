import os
from selenium import webdriver
import time


link = 'http://suninjuly.github.io/file_input.html'
driver = webdriver.Chrome()


try:
    browser = driver
    browser.get(link)
    name = browser.find_element_by_name('firstname')
    name.send_keys('XXXXX')
    last_n = browser.find_element_by_name('lastname')
    last_n.send_keys('XXXXX')
    email = browser.find_element_by_name('email')
    email.send_keys('vanushinaulia@gmail.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    upload = browser.find_element_by_css_selector('input[type="file"]')
    upload.send_keys(file_path)
    button = browser.find_element_by_css_selector('button.btn-primary')
    button.click()
finally:
    time.sleep(2)
    browser.quit()
