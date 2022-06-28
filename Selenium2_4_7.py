from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return math.log(abs(12*math.sin(x)))

browser = webdriver.Chrome()

browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price= WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"),"100"))
button = browser.find_element(By.ID, "book")
button.click()

x_elm = browser.find_element(By.ID, "input_value")
x = int(x_elm.text)
y = calc(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

button = browser.find_element(By.ID, "solve")
button.click()
