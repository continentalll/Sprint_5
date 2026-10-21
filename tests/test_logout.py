import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestLogout:

    def test_logout_success(self, driver):
        driver.get("https://qa-desk.education-services.ru/")
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys("existing@example.com")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("ExistingPass123!")
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(Locators.USER_AVATAR))

        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        wait.until(EC.invisibility_of_element_located(Locators.USER_AVATAR))
        assert driver.find_element(*Locators.LOGIN_REGISTER_BUTTON).is_displayed()