from selenium.webdriver.common.by import By

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_button = (By.XPATH, '//*[@id="menu_button_container"]/div/div[3]/div/button')
        self.logout_link = (By.ID, "logout_sidebar_link")

    def logout(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.logout_link).click()
