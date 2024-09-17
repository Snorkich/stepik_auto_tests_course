from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    inputx = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = inputx.get_attribute("valuex")
    input1 = browser.find_element(By.CSS_SELECTOR, ".form-group #answer")
    input1.send_keys(calc(x))
    input2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    input2.click()
    input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    input3.click()
    input4 = browser.find_element(By.CSS_SELECTOR, ".btn")
    input4.click()


finally:
    time.sleep(10)
    browser.quit()
