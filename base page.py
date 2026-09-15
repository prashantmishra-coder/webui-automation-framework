"""
BasePage - common reusable methods for all Page Objects.
Every page class inherits from this so we don't repeat wait/click/type
logic in every single page file.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=DEFAULT_TIMEOUT):
        """Wait until element is present, then return it."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator, timeout=DEFAULT_TIMEOUT):
        """Wait until element is clickable, then click it."""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type_text(self, locator, text, timeout=DEFAULT_TIMEOUT):
        """Wait for element, clear it, then type text into it."""
        element = self.find(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=DEFAULT_TIMEOUT):
        return self.find(locator, timeout).text

    def is_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False
