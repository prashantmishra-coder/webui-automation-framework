"""
LoginPage - Page Object for the login screen.
Demo site: https://the-internet.herokuapp.com/login
(A public practice site made for exactly this kind of automation demo.)
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    # Locators kept in one place - if the UI changes, only these lines
    # need to be updated, not every test case.
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def load(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def get_flash_message(self):
        return self.get_text(self.FLASH_MESSAGE)
