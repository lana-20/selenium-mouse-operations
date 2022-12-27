from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.import ActionChains

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

...

act = ActionChains(driver)

...

driver.close()
