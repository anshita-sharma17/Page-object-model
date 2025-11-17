# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.saucedemo.com/v1/")
# user_name = driver.find_element(By.ID, "user-name")
# user_name.send_keys("standard_user")
# pass_word = driver.find_element(By.ID, "password")
# pass_word.send_keys("secret_sauce")
# login_btn = driver.find_element(By.ID, "login-button")
# login_btn.send_keys(Keys.ENTER)
# time.sleep(10)
# driver.close()

# pages/login_page.py

# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         # Locators for username, password, and login button
#         self.username_input = (By.ID, "user-name")
#         self.password_input = (By.ID, "password")
#         self.login_button = (By.ID, "login-button")

#     # Method to enter the username
#     def enter_username(self, username):
#         self.driver.find_element(*self.username_input).send_keys(username)

#     # Method to enter the password
#     def enter_password(self, password):
#         self.driver.find_element(*self.password_input).send_keys(password)

#     # Method to click the login button
#     def click_login(self):
#         self.driver.find_element(*self.login_button).send_keys(Keys.ENTER)

# pages/login_page.py

# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.username_input = (By.ID, "user-name")
#         self.password_input = (By.ID, "password")
#         self.login_button = (By.ID, "login-button")

#     def enter_username(self, username):
#         self.driver.find_element(*self.username_input).send_keys(username)

#     def enter_password(self, password):
#         self.driver.find_element(*self.password_input).send_keys(password)


#     def click_login(self):
#         self.driver.find_element(*self.login_button).send_keys(Keys.ENTER)
# from selenium.webdriver.common.by import By


# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.username = (By.ID, "user-name")
#         self.password = (By.ID, "password")
#         self.login_btn = (By.ID, "login-button")

#     def login(self, user, pwd):
#         self.driver.find_element(*self.username).send_keys(user)
#         self.driver.find_element(*self.password).send_keys(pwd)
#         self.driver.find_element(*self.login_btn).click()

# import logging
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoAlertPresentException

# from testcases import test_login

# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.username = (By.ID, "user-name")
#         self.password = (By.ID, "password")
#         self.login_btn = (By.ID, "login-button")
#     def log_details():
#         logging.basicConfig(
#             filename="Logging_file.log",
#             level=logging.INFO,
#             format='%(asctime)s - %(levelname)s - %(message)s',
#             datefmt='%Y-%m-%d  %H:%M:%S  %p'
#         )
#         return logging.getLogger()
#     logger = log_details()
#     logger.info("program execution started")
#         # logger = LogGen.loggen()
#         # logger = logging.getLogger('selenium')
#         # log_path = 'Screenshots/Automation.log'
#         # handler = logging.FileHandler(log_path)
#         # logger.addHandler(handler)

#         # handler = logging.StreamHandler()
#         # logger.addHandler(handler)
#     # def log_details():
#     #     logging.basicConfig(
#     #         filename="Logging_file.log",
#     #         level=logging.INFO,
#     #         format='%(asctime)s - %(levelname)s - %(message)s',
#     #         datefmt='%Y-%m-%d  %H:%M:%S  %p'
#     #     )
#     #     return logging.getLogger()
#     # logger = log_details()
#     # logger.info("program execution started")

#     def loginpage(self, user, pwd):

#         self.driver.find_element(*self.username).send_keys(user)
#         # assert "standard_user" in self.username
#         self.driver.find_element(*self.password).send_keys(pwd)
#         # assert "secret_sauce" in self.password

#         self.driver.find_element(*self.login_btn).click()
#         # logger = LogGen.loggen()


#         try:
#             WebDriverWait(self.driver, 5).until(EC.alert_is_present())
#             alert = self.driver.switch_to.alert
#             alert.accept()
#         except (TimeoutException, NoAlertPresentException):
#             pass
#     logger.info("TEST CASE PASSED")
    
# import logging
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoAlertPresentException

# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.username = (By.ID, "user-name")
#         self.password = (By.ID, "password")
#         self.login_btn = (By.ID, "login-button")
#         self.logger = self.setup_logger()
#         self.logger.info("LoginPage instance initialized.")

#     @staticmethod
#     def setup_logger():
#         logger = logging.getLogger("LoginPageLogger")
#         if not logger.handlers:
#             logger.setLevel(logging.INFO)
#             handler = logging.FileHandler("Logging_file.log")
#             formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
#                                           datefmt='%Y-%m-%d %H:%M:%S %p')
#             handler.setFormatter(formatter)
#             logger.addHandler(handler)
#         return logger

#     def loginpage(self, user, pwd):
#         self.logger.info("Attempting login with provided credentials.")

#         self.driver.find_element(*self.username).send_keys(user)
#         self.driver.find_element(*self.password).send_keys(pwd)
#         self.driver.find_element(*self.login_btn).click()

#         try:
#             WebDriverWait(self.driver, 5).until(EC.alert_is_present())
#             alert = self.driver.switch_to.alert
#             self.logger.warning("Alert present during login, accepting it.")
#             alert.accept()
#         except (TimeoutException, NoAlertPresentException):
#             self.logger.info("No alert appeared during login.")

#         self.logger.info("Login function executed successfully.")
import logging
import inspect
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver


        # Locators for login fields and button
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")

        # Create logger for this class
        self.logger = self.setup_logger()
        self.logger.info("LoginPage initialized.")

    # Setup the logger (writes to file)
    def setup_logger(self):
        logger = logging.getLogger("LoginLogger")
        if not logger.handlers:  # Avoid duplicate logs
            logger.setLevel(logging.INFO)
            file_handler = logging.FileHandler("test_log.log")
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        return logger

    # This method performs the login
    def loginpage(self, user, pwd):
        # Automatically get the test name from the stack
        test_name = inspect.stack()[1].function
        self.logger.info(f"Running test: {test_name}")

        # Perform login steps
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()
        self.logger.info("Clicked login button.")

        # Check for alert pop-up and accept it
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
       
            alert.accept()
            self.logger.warning("Alert appeared and was accepted.")
        except (TimeoutException, NoAlertPresentException):
            self.logger.info("No alert appeared after login.")

        self.logger.info(f"Test '{test_name}' completed.\n")

       