import unittest
import org.openqa.selenium.support.ui.Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class CreditCardPayment(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_cc_payment(self):
        driver = self.driver
        driver.get("https://staging.autobooks.co/pay/autobook-s")
        self.assertIn("Make a payment to Joses", driver.title)
        elem = driver.find_element_by_id("first-name")
        elem.send_keys("Sam")
        elem = driver.find_element_by_id("last-name")
        elem.send_keys("Jones")
        elem = driver.find_element_by_id("description")
        elem.send_keys("testing description")
        elem = driver.find_element_by_id("payment-amount")
        elem.send_keys("10")
        driver.find_element_by_name("payment-schedule-type-select").click()
        elem.selectByVisibleText("One-time payment")
        elem = driver.find_element_by_id("payment-card-name")
        elem.send_keys("Sam Jones")
        elem = driver.find_element_by_id("payment-card-number")
        elem.send_keys("5112000100000003")
        elem = driver.find_element_by_id("payment-card-exp-month")
        elem.send_keys("12")
        elem = driver.find_element_by_id("payment-card-exp-year")
        elem.send_keys("2022")
        elem = driver.find_element_by_id("payment-card-ccv")
        elem.send_keys("111")
        elem = driver.find_element_by_id("payment-card-postal-code")
        elem.send_keys("11222")
        driver.find_element_by_name("terms").click()
        driver.find_element_by_id("submit").click()
        assert "DECLINE" not in driver.page_source


    def tearDown(self):
        self.driver.close()
