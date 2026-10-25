from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urlparse

# Initialize Chrome WebDriver for both local and container execution.
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

def _page_path(url):
    path = urlparse(url).path.rstrip("/")
    return path or "/"


def test_click_item(test_url, target_url, itemname):
    expected_path = _page_path(target_url)

    for attempt in range(1, 4):
        try:
            # Reload the source page for every test and wait for its DOM.
            driver.get(test_url)
            WebDriverWait(driver, 20).until(
                lambda browser: browser.execute_script("return document.readyState") == "complete"
            )

            # Match the stable destination, not case-sensitive visible text.
            page_name = expected_path.rsplit("/", 1)[-1]
            if page_name in ("", "index.html"):
                link_xpath = "//a[contains(@href, 'index.html') or @href='/']"
            else:
                link_xpath = f"//a[contains(@href, '{page_name}')]"

            link_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, link_xpath))
            )
            driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'}); arguments[0].click();",
                link_element,
            )

            WebDriverWait(driver, 20).until(
                lambda browser: _page_path(browser.current_url) == expected_path
            )
            print(f"Link test for {itemname} at URL {target_url} passed successfully!", flush=True)
            print("Attempting the next test for the next item in the array...", flush=True)
            return "PASS"

        except (TimeoutException, WebDriverException) as err:
            if attempt == 3:
                print(
                    f"An error occurred trying to perform the test for {itemname} "
                    f"after {attempt} attempts: {err}",
                    flush=True,
                )
                return "FAIL"

    return "FAIL"

def close_browser():
    driver.quit()

