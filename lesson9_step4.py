from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.TAG_NAME, "button").click()
    alert = browser.switch_to.alert
    alert.accept()
    valuex = browser.find_element(By.ID, "input_value").text
    inputx = calc(valuex)
    browser.find_element(By.ID, "answer").send_keys(inputx)
    input1 = browser.find_element(By.CSS_SELECTOR, ".btn")
    input1.click()

finally:
    time.sleep(10)
    browser.quit()
