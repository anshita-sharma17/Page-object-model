
# from selenium.webdriver.common.by import By

# class CartPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.cart_button = (By.ID, 'shopping_cart_container') 

#     def click_cart_button(self):
#         self.driver.find_element(*self.cart_button).click()


# from selenium.webdriver.common.by import By

# class CartPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.checkout_btn = (By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_footer > a.btn_action.checkout_button")

#     def click_cart(self):
#         self.driver.find_element(*self.cart_btn)

from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_btn = (By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_footer > a.btn_action.checkout_button") 

    def click_checkout(self):
        self.driver.find_element(*self.checkout_btn).click()


