from selenium import webdriver
# from selenium.webdriver import Keys

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = "D:\\zPersonal\\Projects\\2Minions\\webdriver\\chromedriver.exe")

driver.get("https://greenpixie.com/website-carbon-calculator")

# elem = driver.find_element_by_class_name(value="dkoKSk")
elem = driver.find_element(By.CLASS_NAME, "SiteInput__Input-sc-1uamvxq-1 dkoKSk")

elem.clear()
elem.send_keys("https://chromedriver.chromium.org/downloads")
elem.send_keys(Keys.RETURN)

driver.quit()