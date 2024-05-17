import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager import ChromeDriverManager
import time
import XLUtensils

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", "true")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install(), options=options))
driver.get("https://demo.guru99.com/test/newtours/")
path = r"C:\Users\lenovo\Downloads\datadriven.xlsx"
rows = XLUtensils.get_row_count(path, 'Sheet1')
for r in range(2, rows + 1):
    username = XLUtensils.read_data(path, 'Sheet1', r, 1)
    password = XLUtensils.read_data(path, 'Sheet1', r, 2)
    driver.implicitly_wait(10)

    driver.find_element(By.XPATH, "//input[@name='userName']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@name='submit']").click()
    if driver.title == "Login: Mercury Tours":
        print("test is passed")
        XLUtensils.write_data(path,'Sheet1',r,3)
    else:
        print("test is failed")
        XLUtensils.write_data(path, 'Sheet1', r, 3)

