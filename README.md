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

    driver.get("https://www.amazon.com/")
    driver.find_element(By.XPATH, "//span[@class='nav-line-2 ']")	# Account & List tab

...



