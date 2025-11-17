# from selenium.webdriver.common.by import By

# class CheckPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.check_button = (By.ID, 'btn_action checkout_button') 

#     def click_check_button(self):
#         self.driver.find_element(*self.check_button_button).click()

from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_btn = (By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[2]/input')
        self.finish_btn = (By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]/a[2]')

    def fill_details_and_continue(self, fname, lname, postal):
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(postal)
        self.driver.find_element(*self.continue_btn).click()
        

    def finish_checkout(self):
        self.driver.find_element(*self.finish_btn).click()

