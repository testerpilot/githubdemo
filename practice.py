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

driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.ID, "name").send_keys("automate tester")
driver.find_element(By.ID, "email").send_keys("testing@gmail.com")
driver.find_element(By.ID, "phone").send_keys("12345667888")
driver.find_element(By.ID, "textarea").send_keys("germany")
driver.find_element(By.ID, "female").click()

# checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
# for checkbox in checkboxes:
#     day = checkbox.get_attribute('id')
#     if day == 'sunday' or day == 'friday':
#         checkbox.click()
driver.find_element(By.XPATH,"//input[@id='tuesday']").click()
dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text("India")

datepicker=driver.find_element(By.ID,"datepicker")
datepicker.clear()
datepicker.send_keys("10/05/1991")
datepicker.send_keys(Keys.RETURN)

driver.find_element(By.LINK_TEXT,"Home").click()
driver.find_element(By.XPATH,"//tbody/tr[1]/td[4]/input[1]").click()
time.sleep(3)
driver.close()

