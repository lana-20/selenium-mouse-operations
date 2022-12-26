from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://carbon38.com/collections/sale")
sale_item = driver.find_element(By.XPATH, "(//li[@class='isp_grid_product inventory'])[1]")

...

driver.close()
