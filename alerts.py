from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", "true")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install(), options=options))
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']").click()
alert = driver.switch_to.alert
alert.accept()
