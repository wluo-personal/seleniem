
import undetected_chromedriver.v2 as uc
import time


PATH = "../driver/chromedriver"



# chrome_options = Options()
# chrome_options.add_argument("--enable-javascript")


driver = uc.Chrome()
# driver = uc.Chrome(driver_executable_path="../driver/chromedriver")
driver.get("https://www.ticketmaster.com/")
time.sleep(300)
print(driver.title)