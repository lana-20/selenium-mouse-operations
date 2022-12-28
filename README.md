# Selenium Mouse Operations

Sometimes, as an SDET, I work with various mouse operations in an app. Operations, such as like drag and drop, right click, or double click. 

To handle mouse operations in Selenium, I use a WebDriver class called [ActionChains()](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html). This class avails a number if methods to perform double click, right click, or drag and drop.

Different types of mouse related operations:
1) Mouse hover - _move_to_element()_
2) Right click - _context_click(element)_
3) Double click
4) Drag and drop

Apart from this, there are different types of scenarios where I can use a mouse operation. Eg, I find a slider where I can drag and drop that slider from one place to another. This is also considered a mouse related operation.

I encounter mouse hover actions in some apps. As soon as I place my mouse cursor on a particular element, some other hidden sub-menu options are diplayed. 

Login to the www.amazon.com account. As soon as I hover over the Accounts & Lists tab, some other menus pop up to choose options for shopping. I can click on previously purchased items or manage those items, click on one of my lists or create a list (Wishlist, Alexa shopping list, registry, etc.), or select any of the account options.

<img src="https://user-images.githubusercontent.com/70295997/209458367-19d7d2f7-3c72-4108-8499-60096052e3c3.png" width=800>

Mouse over action is placing the mouse cursor on a particular element. Then the sub-options get displyed, I am able to see and interact with the rest of elements.

Another e-commerce app example is Carbon38, a performance fashion store. Here my operation is to go to a sale item, then the Quick Shop view, and verify the Add to Bag button is loaded in the DOM. So, I move my cursor over the 1st inventory item, then click on the Quick Shop button to display the quick view element. Then I use the WebDriverWait and [Expected Conditions](https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html) to verify the Add to Cart button is clickable (visible and enabled such that I can click it). Additional validations are possible, but I focus on the mouse actions.

Go to https://carbon38.com/collections/sale and hover over the 1st sale items in the inventory list.

    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service as ChromeService

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://carbon38.com/collections/sale")
    sale_item = driver.find_element(By.XPATH, "(//li[@class='isp_grid_product inventory'])[1]")

<img src="https://user-images.githubusercontent.com/70295997/209482028-1261765d-d5b2-4042-ba8e-bf632b03746a.png" width=800>

Click the Quickshop button.

    (//a[@class='isp_product_quick_view_button'])[1]

<img src="https://user-images.githubusercontent.com/70295997/209482035-e9e1302f-4118-492e-bcd4-46964afe5ac8.png" width=800>

Observe the Quickview element appear:

    //div[@id='isp_product_quick_view_model']

<img src="https://user-images.githubusercontent.com/70295997/209588096-9c729fa9-ab88-4b6e-99c9-7e986b62cc48.png" width=800>

Verify Add to Bag button is displayed.

    //button[@class='isp_quick_view_add_to_cart_btn_quick_view']

<img src="https://user-images.githubusercontent.com/70295997/209482051-8935aee7-a2f5-4966-83df-590b37d6c017.png" width=800>

To perfrom the mouse hover action I need to create an [ActionChains()](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains) class object, because I can't directly access methods from the this class. It's a built-in class available in Selenium WebDriver. Through the object of the class I am able to access all the methods which perform the mouse operations. Pass the driver into the object. To mouse over, I use the _move_to_element()_ method and pass into it the element I want to move to.

I create chained actions to be performed. To actually perform these actions, I add the _perform()_ method. No actions get perfomred without this method. To mouse over one element, one _move_to_element()_ statement suffices.

        from selenium.webdriver.import ActionChains

        ...

        quickshop_btn = driver.find_element(By.XPATH, "(//a[@class='isp_product_quick_view_button'])[1]")
        add_to_cart = driver.find_element(By.XPATH, "//button[@class='isp_quick_view_add_to_cart_btn_quick_view']")

        act = ActionChains(driver)
        act.move_to_element(sale_item).click(quickshop_btn).perform()

        assertEqual("ADD TO BAG", add_to_cart.text)

Some apps do not allow to perform a click action on the tabs. In those case, I use the mouse hover option.

Sometimes I need to perform the right click action. Let's explore another app https://swisnl.github.io/jQuery-contextMenu/demo.html.

When I click on the 'right click me' button, nothing happens. But when I right click on the button, I can see a few options - Edit, Cut, Copy, Paste, Delete, Quit. I can click on any of these options, but only after I right click on the button. The _.click()_ method does not work on the button element, because it is associated with the right click functionality. A regular manual click also triggers nothing.

<img src="https://user-images.githubusercontent.com/70295997/209598772-726b81ac-de78-4101-b19c-55eb9ef1d56e.png" width=800>

I can inspect and capture the button, but do not get the inspect option for the submenu elements that display upon a right click. I still want to locate these elements by a certain number of attributes. To get the attributes, right click anywhere on the web page, click Inspect to display DOM in the DevTools Elements tab. Click on the inspector option arrow mark and show the desired element(s).

<img src="https://user-images.githubusercontent.com/70295997/209858979-13ccb209-6875-45db-80a2-12af00402c85.png" width=400>

<img src="https://user-images.githubusercontent.com/70295997/209859019-7c254f24-4ac7-4f8f-8593-db4d3e1bd221.png" width=800>


    driver.implicitly_wait(10)
    driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    driver.maximize_window()

    btn = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

As soon as I capture the button I need to perform the right click as a mouse action. Create an ActionChains() class object and pass the driver instance into it.

    act = ActionChains(driver)

To perform the right click action on the button, I have to access the _.context_click()_ method by using the _act_ object. Pass the element, on which the action gets peformed. This merely creates an action. To peform the action append the mandatory _.perform() method.

    act.context_click(btn).perform()

Now, let's learn how to perform the double click action in this app https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3.

A simple form is available on the right side. Field 1 has some text displayed, Field 2 is emply. When I peform a normal click on the 'Copy Text' button, nothing happens. But when I do a double click, the text get copied from the 1st to the 2nd text box. This happens only upon the double click action.

I can also change the data. Eg, I can type 'Welcome' in Field 1 and copy it to Field 2. This button has a double click functionality associated with it.

2 click actions do not equal 1 double click action. Double click is a different type of action

I clear the 1st textbox, pass some value into it, and double click the button element to copy the value to the 2nd textbox. All these elements are located within a frame. To interact with these elements, first, I have to switch to this particular frame. I can directly pass the frame id or name into the switching command. That automatically switches me to the form.

<img src="https://user-images.githubusercontent.com/70295997/209875590-4d5afc46-cdf7-478a-8e3a-7bb490e50a5e.png" width=800>


    driver.switch_to.frame("iframeResult")

    field1 = driver.find_element(By.XPATH, "//input[@id='field1']")
    field1.clear().send_keys("welcome")
    field2 = driver.find_element(By.XPATH, "//input[@id='field2']")
    # btn = driver.find_element(By.XPATH, "//button[@ondblclick='myFunction()']")

    act = ActionChains(driver)






