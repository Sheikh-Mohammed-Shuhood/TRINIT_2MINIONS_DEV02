import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

x=sys.argv[1] 

driver = webdriver.Chrome(executable_path = "D:\\zPersonal\\Projects\\2Minions\\webdriver\\chromedriver.exe")

driver.get("https://greenpixie.com/website-carbon-calculator")

elem = driver.find_element(By.CLASS_NAME, "SiteInput__Input-sc-1uamvxq-1")

elem.clear()
elem.send_keys(x)
elem.send_keys(Keys.RETURN)
time.sleep(30)

recvelem = driver.find_element(By.CLASS_NAME, 'ResultBox__ResultBoxHighlightText-sc-bw8194-7')
my_value = recvelem.text
print("less than "+str(my_value))
driver.quit()
