from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Ivanovich")
    browser.find_element(By.NAME, "email").send_keys("12345@email.com")

    buttonin = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')
    buttonin.send_keys(file_path)

    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(20)
    browser.quit
