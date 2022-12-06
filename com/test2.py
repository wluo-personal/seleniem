from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

PATH = "../driver/chromedriver"


#
# chrome_options = Options()
# chrome_options.add_argument('--disable-blink-features=AutomationControlled')
# chrome_options.add_argument("--enable-javascript")
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)
#
#
# driver = webdriver.Chrome(
#     executable_path=PATH,
#     chrome_options=chrome_options
#                           )
# driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.012; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r'PATH')
# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
# driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
print(driver.execute_script("return navigator.userAgent;"))

driver.get("https://www.ticketmaster.com/")
print(driver.title)

# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.NAME, "q"))
# )
time.sleep(300)
element = driver.find_element(by=By.NAME, value="q")
element.send_keys("林俊杰 2023 演唱会")
time.sleep(300)
element.send_keys(Keys.RETURN)


time.sleep(10)
d = 1


