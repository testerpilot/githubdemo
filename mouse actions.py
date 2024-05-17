from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager import ChromeDriverManager
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("https://lambdalabs.com/")
driver.maximize_window()
driver.implicitly_wait(10)

cloud =driver.find_element(By.XPATH,"//a[@href='https://lambdalabs.com/service/gpu-cloud'][normalize-space()='Cloud']").click()
cloudsignin=driver.find_element(By.XPATH,"//span[normalize-space()='Cloud Sign-In']").click()
ondemandcloud=driver.find_element(By.XPATH,"//span[normalize-space()='On Demand Cloud']").click()
reversecloud = driver.find_element(By.XPATH, "//span[normalize-space()='Reserved Cloud']").click()

actions = ActionChains(driver)
actions.move_to_element(cloud).move_to_element(cloudsignin).move_to_element(ondemandcloud).move_to_element(reversecloud).click().perform()
driver.close()
driver.switch_to.al