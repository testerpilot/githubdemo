from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager import ChromeDriverManager

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("https://docs.oracle.com/javase/8/docs/api/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.switch_to.frame("packageListFrame")
driver.find_element(By.XPATH, "//a[normalize-space()='java.awt.datatransfer']").click()
driver.switch_to.default_content()
driver.implicitly_wait(10)
driver.switch_to.frame("packageFrame")
driver.find_element(By.XPATH, "//span[normalize-space()='ItemSelectable']").click()
