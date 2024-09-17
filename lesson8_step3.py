from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.ID, "num1")
    input2 = browser.find_element(By.ID, "num2")

    number1 = input1.text
    number2 = input2.text
    x = int(number1) + int(number2)

    select = Select(browser.find_element(By.TAG_NAME, "select")) 
    select.select_by_value(str(x))

    browser.find_element(By.CLASS_NAME, "btn").click()


finally:
    time.sleep(10)
    browser.quit()
