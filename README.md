# Selenium Mouse Operations

Sometimes, as an SDET, I work with various mouse operations in an app. Operations, such as like drag and drop, right click, or double click. 

To handle mouse operations in Selenium, I use a WebDriver class called ActionChains(). This class avails a number if methods to perform double click, right click, or drag and drop.

Different types of mouse related operations:
1) Mouse hover
2) Right click
3) Double click
4) Drag and drop

Apart from this, there are different types of scenarios where I can use a mouse operation. Eg, I find a slider where I can drag and drop that slider from one place to another. This is also considered a mouse related operation.

I encounter mouse hover actions in some apps. As soon as I place my mouse cursor on a particular element, some other menu options are diplayed. 

Login to the www.amazon.com account. As soon as I hover over the Accounts & Lists tab, some other menus pop up to choose options for shopping. I can click on previously purchased items or manage those items, click on one of my lists or create a list (Wishlist, Alexa shopping list, registry, etc.), or select any of the account options.

<img src="https://user-images.githubusercontent.com/70295997/209458367-19d7d2f7-3c72-4108-8499-60096052e3c3.png" width=800>

Mouse over action is placing the mouse cursor on a particular element. Then the sub-options get displyed, I am able to see and interact with the rest of elements.

Another e-commerce app example is Carbon38, a performance fashion store. Here my operation is to go to a sale item, then the Quick Shop view, and verify the Add to Bag button is loaded in the DOM. So, I move my cursor over the 1st inventory item, then click on the Quick Shop button to display the quick view element. Then I use the WebDriverWait and [Expected Conditions](https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html) to verify the Add to Cart button is clickable (visible and enabled such that I can click it). Additional validations are possible, but I focus on the mouse actions.

Go to https://carbon38.com/collections/sale and hover over the 1st sale items in the inventory list.

    driver.get("https://carbon38.com/collections/sale")
    sale_item = driver.find_element(By.XPATH, "(//li[@class='isp_grid_product inventory'])[1]")

<img src="https://user-images.githubusercontent.com/70295997/209482028-1261765d-d5b2-4042-ba8e-bf632b03746a.png" width=800>

Click the Quickshop button. (INSERT action chains class code)

    quickshop_btn -> (//a[@class='isp_product_quick_view_button'])[1]

<img src="https://user-images.githubusercontent.com/70295997/209482035-e9e1302f-4118-492e-bcd4-46964afe5ac8.png" width=800>

Capture the Quickview element:

    //div[@id='isp_product_quick_view_model']

<img src="https://user-images.githubusercontent.com/70295997/209482044-a6dc2b8e-f51e-4be8-830d-c83dc46fec24.png" width=800>

Verify Add to Bag button is displayed.

    //button[@class='isp_quick_view_add_to_cart_btn_quick_view']

<img src="https://user-images.githubusercontent.com/70295997/209482051-8935aee7-a2f5-4966-83df-590b37d6c017.png" width=800>




