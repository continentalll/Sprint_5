import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestAdvertisement:

    def test_create_ad_unauthorized(self, driver):
        driver.get("https://qa-desk.education-services.ru/")
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(Locators.PLACE_AD_BUTTON)).click()

        modal = wait.until(EC.visibility_of_element_located(Locators.AUTH_REQUIRED_MODAL))
        assert modal.text == "Чтобы разместить объявление, авторизуйтесь"

    def test_create_ad_authorized(self, driver):
        driver.get("https://qa-desk.education-services.ru/")
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys("existing@example.com")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("ExistingPass123!")
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(Locators.USER_AVATAR))

        wait.until(EC.element_to_be_clickable(Locators.PLACE_AD_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(Locators.AD_NAME_INPUT)).send_keys("Тестовое объявление")
        driver.find_element(*Locators.AD_DESCRIPTION_INPUT).send_keys("Описание тестового объявления")
        driver.find_element(*Locators.AD_PRICE_INPUT).send_keys("999")

        wait.until(EC.element_to_be_clickable(Locators.CATEGORY_DROPDOWN)).click()
        wait.until(EC.element_to_be_clickable(Locators.CATEGORY_OPTION_TECHNOLOGIES)).click()

        wait.until(EC.element_to_be_clickable(Locators.CITY_DROPDOWN)).click()
        wait.until(EC.element_to_be_clickable(Locators.CITY_OPTION_SPB)).click()

        condition_input = wait.until(EC.presence_of_element_located(Locators.CONDITION_NEW_INPUT))
        driver.execute_script("arguments[0].click();", condition_input)

        wait.until(EC.element_to_be_clickable(Locators.PUBLISH_BUTTON)).click()

        wait.until(EC.element_to_be_clickable(Locators.PROFILE_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(Locators.MY_ADS_BLOCK))
        ad_card = wait.until(EC.visibility_of_element_located(Locators.AD_CARD))
        assert "Тестовое объявление" in ad_card.text