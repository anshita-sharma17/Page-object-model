# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from PIL import Image
# import time

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.saucedemo.com/v1/")
# from conftest import Config
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# from PIL import Image

# driver = webdriver.Chrome()

# driver.implicitly_wait(10)
# products = driver.find_element(By.ID, "btn_primary btn_inventory")
# products.driver.send_keys(Keys.ENTER)
# screenshot_path = r'C:\Users\MY PC\POM\Screenshots\mainpage.png'
# driver.save_screenshot(screenshot_path)
# screenshot = Image.open(screenshot_path)
# screenshot.show()
# time.sleep(5)
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# from PIL import Image
# driver = webdriver.Chrome()

# driver.get(Config.BASE_URL)
# driver.implicitly_wait(10) 

# products = driver.find_element(By.CLASS_NAME, "btn_primary") 

# products.send_keys(Keys.ENTER)

# time.sleep(2)
# screenshot_path = r'C:\Users\MY PC\POM\Screenshots\mainpage.png'
# driver.save_screenshot(screenshot_path)

# screenshot = Image.open(screenshot_path)
# screenshot.show()

# time.sleep(5)
# driver.quit()
# pages/order_page.py

# from selenium.webdriver.common.by import By

# class OrderPage:
#     def __init__(self, driver):
#         self.driver = driver
#         # Main "Add to cart" buttons ke liye locator
#         self.products_button = (By.CLASS_NAME, "btn_primary")

#     def click_products_button(self):
#         # Page pe pehla "Add to cart" button click karega
#         self.driver.find_element(*self.products_button).click()

#     def get_page_title(self):
#         return self.driver.title

# from selenium.webdriver.common.by import By

# class OrderPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.item_titles = (By.CLASS_NAME, "inventory_item_name")  # or update with correct locator

#     def click_on_exact_product(self, expected_name):
#         items = self.driver.find_elements(*self.item_titles)
#         for item in items:
#             if item.text.strip() == expected_name:
#                 item.click()
#                 return True  # success
#         return False  # item not found

from selenium.webdriver.common.by import By

# class OrderPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.products_button = (By.CLASS_NAME, "")

#     def click_products_button(self):
#         self.driver.find_element(*self.products_button).click()

    # def get_page_title(self):
    #     return self.driver.title

from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product(self, product_name):
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for product in products:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            print(name)
            if product_name == name:
                product.find_element(By.CLASS_NAME, "btn_inventory").click()
                print(f"Added product: {name}")
                break

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()



