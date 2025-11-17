# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.saucedemo.com/v1/")


# import pytest
# from selenium import webdriver

# @pytest.fixture(scope="function")
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()

# conftest.py

# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from PIL import Image

# @pytest.fixture
# def setup():
#     chrome_options = Options()
#     chrome_options.add_argument("--start-maximized")  
#     driver = webdriver.Chrome(options=chrome_options)

#     yield driver

#     driver.quit()

# import pytest
# from selenium import webdriver
# from PIL import Image

# @pytest.fixture
# def setup():
#     driver = webdriver.Chrome()
#     driver.maximize_window

#     yield driver
#     driver.quit()

# conftest.py
# import pytest
# from selenium import webdriver

# @pytest.fixture
# def setup():
#     driver = webdriver.Chrome()  # chromedriver agar system PATH me hai to direct chalega
#     driver.maximize_window()
#     yield driver
#     driver.quit()








