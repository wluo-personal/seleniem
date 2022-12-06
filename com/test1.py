from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "../driver/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.ticketmaster.com/")
print(driver.title)

# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.NAME, "q"))
# )
time.sleep(30)
element = driver.find_element(by=By.NAME, value="q")
element.send_keys("林俊杰 2023 演唱会")
time.sleep(300)
search.send_keys(Keys.RETURN)


time.sleep(10)
d = 1


