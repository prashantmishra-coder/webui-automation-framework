"""
test_login.py - regression tests for the login flow.
Uses pytest.mark.parametrize to run the same test logic against
multiple data sets (data-driven testing) from utils/test_data.py.
"""

import pytest
from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from utils.test_data import LOGIN_TEST_DATA


@pytest.mark.parametrize(
    "username, password, expect_success, expected_message", LOGIN_TEST_DATA
)
def test_login(driver, username, password, expect_success, expected_message):
    login_page = LoginPage(driver).load()
    login_page.login(username, password)

    if expect_success:
        secure_page = SecurePage(driver)
        assert secure_page.is_visible(secure_page.PAGE_HEADER)
        message = login_page.get_flash_message()
    else:
        message = login_page.get_flash_message()

    assert expected_message in message, (
        f"Expected '{expected_message}' in flash message, got: '{message}'"
    )


def test_logout(driver):
    login_page = LoginPage(driver).load()
    login_page.login("tomsmith", "SuperSecretPassword!")

    secure_page = SecurePage(driver)
    secure_page.logout()

    message = login_page.get_flash_message()
    assert "You logged out" in message
