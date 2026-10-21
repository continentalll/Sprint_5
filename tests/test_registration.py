import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestRegistration:

    def test_registration_success(self, driver, unique_email):
        driver.get("https://qa-desk.education-services.ru/")
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys(unique_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("Qwerty123!")
        driver.find_element(*Locators.REPEAT_PASSWORD_INPUT).send_keys("Qwerty123!")
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        user_name = wait.until(EC.visibility_of_element_located(Locators.USER_NAME))
        assert user_name.text == "User."

    def test_registration_invalid_email_error_message(self, driver):
        driver.get("https://qa-desk.education-services.ru/")
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys("invalidemail")
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        error_msg = wait.until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE))
        assert error_msg.text == "Ошибка"

    def test_registration_existing_user_error_message(self, driver, unique_email):
        driver.get("https://qa-desk.education-services.ru/")
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys(unique_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("Qwerty123!")
        driver.find_element(*Locators.REPEAT_PASSWORD_INPUT).send_keys("Qwerty123!")
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        wait.until(EC.visibility_of_element_located(Locators.USER_AVATAR))

        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON))

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys(unique_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("Qwerty123!")
        driver.find_element(*Locators.REPEAT_PASSWORD_INPUT).send_keys("Qwerty123!")
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        error_msg = wait.until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE))
        assert error_msg.text == "Ошибка"