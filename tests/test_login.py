import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebDriverWrapper
from utilities import data_source


class TestLogin(WebDriverWrapper):
    def test_valid_login(self):
        self.driver.find_element(By.XPATH, "//span[@class='hicon fa fa-user-o']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Phone Number']").send_keys("999999999")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Proceed']").click()
        result = self.driver.find_element(By.XPATH, "//button[normalize-space()='Resend OTP']").text

        assert_that("Resend OTP").is_equal_to(result)

    """Invalid Login Test - Data Driven Using .csv file"""

    @pytest.mark.parametrize("mobile,error", data_source.test_invalid_login_data)
    def test_invalid_login(self, mobile,error):
        self.driver.find_element(By.XPATH, "//span[@class='hicon fa fa-user-o']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Phone Number']").send_keys("999999999")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Proceed']").click()
        result = self.driver.find_element(By.XPATH, "//u[@class='xsmbl']").text

        assert_that("Create Account").is_equal_to(result)
