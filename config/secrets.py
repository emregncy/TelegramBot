from selenium import webdriver
from selenium.webdriver.commong.keys import Keys
import time
import ConfigParser

chromedriver = "/mnt/c/Users/emreg/Downloads/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(driver_path)

driver.get("https://isikuniversity.mrooms.net/login/index.php")

emailInput = driver.find_element("name", "username")
paswrdInput = driver.find_element("name", "password")
config = ConfigParser.ConfigParser()
config.read('config.json')
emailInput.send_keys(config.get('config', 'student_email'))
paswrdInput.send_keys(config.get('config', 'student_password'))
paswrdInput.send_keys(Keys.RETURN)

## time.sleep(5) bu mainde olacak


## driver.quit() bu da mainde olacak
    
