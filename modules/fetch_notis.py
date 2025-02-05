from selenium import webdriver
from selenium.webdriver.commong.keys import Keys

driver.get("https://isikuniversity.mrooms.net/message/output/popup/notifications.php")

notifications = driver.find_element("class", "dropdown-item")
notifications2 = driver.find_element("role", "menuitem")

for notification in notifications, notifications2:
    print(notifications.text.strip())
