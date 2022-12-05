from selenium import webdriver

PATH = "../driver/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://google.com")
print(driver.title)

d = 1


