"""
Test data kept separate from test logic - this is what makes the suite
'data-driven'. Add more rows here to add more test scenarios without
touching the test code itself.
"""

# (username, password, expect_success, expected_message_snippet)
LOGIN_TEST_DATA = [
    ("tomsmith", "SuperSecretPassword!", True, "You logged into a secure area"),
    ("wrong_user", "SuperSecretPassword!", False, "Your username is invalid"),
    ("tomsmith", "wrong_password", False, "Your password is invalid"),
]
