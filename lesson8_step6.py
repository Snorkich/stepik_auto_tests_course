from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    inputx = browser.find_element(By.ID, "input_value")
    valuex = inputx.text

    browser.find_element(By.ID, "answer").send_keys(calc(valuex))

    browser.find_element(By.ID, "robotCheckbox").click()
    button1 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1.click()
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(20)
    browser.quit
