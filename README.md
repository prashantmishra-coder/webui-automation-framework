# Web UI Automation Framework (Python + Selenium + Pytest)

A modular, data-driven regression testing framework built with Python, Selenium WebDriver, and Pytest, following the Page Object Model (POM) design pattern.

Demo target: SauceDemo (https://www.saucedemo.com/) — a public e-commerce demo site used for practicing Selenium automation (login, inventory, cart, checkout flows).

## Features
- Page Object Model (POM)
- Reusable utilities — centralized explicit waits, driver setup/teardown
- Data-driven tests
- HTML test reports via pytest-html
- Config-driven (base URL, browser, timeouts)
- CI-ready headless Chrome support

## Setup
pip install -r requirements.txt

## Running Tests
pytest --html=reports/report.html --self-contained-html

## Tech Stack
Python 3.10+, Selenium WebDriver 4.x, Pytest, pytest-html, webdriver-manager
