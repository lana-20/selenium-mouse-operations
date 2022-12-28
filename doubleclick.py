from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.import ActionChains

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()

driver.switch_to.frame("iframeResult")

field1 = driver.find_element(By.XPATH, "//input[@id='field1']")
field1.clear.send_keys("welcome")
field2 = driver.find_element(By.XPATH, "//input[@id='field2']")

# btn = driver.find_element(By.XPATH, "//button[@ondblclick='myFunction()']")

act = ActionChains(driver)
act.double_click(btn).perform()

driver.close()
