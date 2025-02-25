import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_check_credit_balance(browser):
    # Navigate to the payment gateway homepage
    browser.get("https://demo.guru99.com/payment-gateway/index.php")
    time.sleep(2)

    # Click on 'Check Credit Card Limit' link
    browser.find_element(By.LINK_TEXT, "Check Credit Card Limit").click()
    time.sleep(5)

    # Input credit card number
    browser.find_element(By.NAME, "card_number").send_keys("1234567890123456")

    # Click on Submit
    browser.find_element(By.NAME, "submit").click()
    time.sleep(5)

    # Verify if the credit card balance is displayed
    assert "Credit Card Balance" in browser.page_source, "Failed to retrieve credit card balance!"
