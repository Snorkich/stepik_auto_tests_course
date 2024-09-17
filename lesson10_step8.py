from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book").click()
    

    valuex = browser.find_element(By.ID, "input_value").text
    inputx = calc(valuex)
    browser.find_element(By.ID, "answer").send_keys(inputx)
    input1 = browser.find_element(By.ID, "solve")
    input1.click()


finally:
    time.sleep(25)
    browser.quit()
