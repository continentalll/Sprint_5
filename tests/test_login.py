import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestLogin:

    def test_login_success(self, driver):
        driver.get("https://qa-desk.education-services.ru/")
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys("existing@example.com")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("ExistingPass123!")
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        wait.until(EC.visibility_of_element_located(Locators.USER_AVATAR))
        assert driver.find_element(*Locators.USER_NAME).is_displayed()