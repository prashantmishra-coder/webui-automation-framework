"""
conftest.py - shared pytest fixtures.
The 'driver' fixture creates a fresh browser for every test and
guarantees it's closed afterwards, even if the test fails.
"""

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    drv = webdriver.Chrome()
    drv.maximize_window()
    yield drv
    drv.quit()
