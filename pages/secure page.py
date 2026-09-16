"""
SecurePage - Page Object for the page shown after a successful login.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SecurePage(BasePage):
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.button.secondary")
    PAGE_HEADER = (By.TAG_NAME, "h2")

    def get_header_text(self):
        return self.get_text(self.PAGE_HEADER)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)
