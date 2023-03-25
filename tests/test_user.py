import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebDriverWrapper
from utilities import data_source


class TestAddEmployee(WebDriverWrapper):
    @pytest.mark.parametrize('first_name,last_name,email_id,password,confirm_password,mobile,expected_error',
                             data_source.test_invalid_user)
    def test_invalid_user(self,first_name,last_name,email_id,password,confirm_password,mobile,expected_error):
        self.driver.find_element(By.XPATH, "//span[@class='hicon fa fa-user-o']").click()
        self.driver.find_element_by_css_selector(".xsmbl").click()
        self.driver.find_element_by_css_selector("input[placeholder='First Name *']").send_keys(first_name)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys(last_name)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email ID *']").send_keys(email_id)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Choose New Password *']").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Confirm Password *']").send_keys(confirm_password)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Mobile Number(For order status update) *']").send_keys(mobile)
        self.driver.find_element(By.XPATH, "//label[@class='form-check-label']//label[1]").click()
        actual_error = self.driver.find_element(By.XPATH, "//div[contains(text(),'Not matched.')]").text
        assert_that(actual_error).contains(expected_error)

    @pytest.mark.parametrize(
        "first_name,last_name,email_id,password,confirm_password,mobile,expected_error",
        data_source.test_valid_user
    )
    def test_add_valid_employee(self, first_name,last_name,email_id,password,confirm_password,mobile,expected_error):
        self.driver.find_element(By.XPATH, "//span[@class='hicon fa fa-user-o']").click()
        self.driver.find_element_by_css_selector(".xsmbl").click()
        self.driver.find_element_by_css_selector("input[placeholder='First Name *']").send_keys(first_name)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys(last_name)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email ID *']").send_keys(email_id)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Choose New Password *']").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Confirm Password *']").send_keys(confirm_password)
        self.driver.find_element(By.XPATH,
                                 "//input[@placeholder='Mobile Number(For order status update) *']").send_keys(mobile)
        self.driver.find_element(By.XPATH, "//label[@class='form-check-label']//label[1]").click()
        actual_error = self.driver.find_element(By.XPATH, "//div[contains(text(),'Must have 6 characters at least.')]").text
        assert_that(actual_error).contains(expected_error)
