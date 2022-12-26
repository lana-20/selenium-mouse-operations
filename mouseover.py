from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.import ActionChains

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://carbon38.com/collections/sale")

sale_item = driver.find_element(By.XPATH, "(//li[@class='isp_grid_product inventory'])[1]")
quickshop_btn = driver.find_element(By.XPATH, "(//a[@class='isp_product_quick_view_button'])[1]")
add_to_cart = driver.find_element(By.XPATH, "//button[@class='isp_quick_view_add_to_cart_btn_quick_view']")

act = ActionChains()
act.move_to_element(sale_item).move_to(quickshop_btn).click().perform()
assertEqual("ADD TO BAG", add_to_cart.text)

...

driver.close()
