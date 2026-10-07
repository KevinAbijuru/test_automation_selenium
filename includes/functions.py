from binascii import Error

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

def test_click_item(test_url, target_url, itemname):
    try:
        # 1. Open the target webpage
        driver.get(test_url)
        driver.maximize_window()

        # 2. Locate the link (by its visible text or XPath)
        # Strategy A: Using the exact text displayed on the page
        link_element = driver.find_element(By.LINK_TEXT, itemname)
        
        # Strategy B: Alternative using XPath if the text is dynamic
        # link_element = driver.find_element(By.XPATH, "//a[@id='myLink']")

        # 3. Click the link
        link_element.click()
        time.sleep(2) # Brief pause to allow the page to load

        # 4. Verify navigation by checking the current URL
        expected_url = target_url  # Assuming itemname is the expected URL after clicking
        assert driver.current_url == expected_url, f"Expected {expected_url} but got {driver.current_url}"
        print(f"Link test for {itemname} at URL {target_url} passed successfully!")
        print(f"Attempting the next test for the next item in the array...")

    except Error as err:
        print(f"An error occurred trying to perform the test:  {err}")
    return None

    #Close the broswer after the test
    close_browser()

def close_browser():
    driver.quit()
