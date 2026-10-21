import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
import string


def generate_email():
    domen = random.choice(["example.com", "test.ru", "mail.ru"])
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for _ in range(10))
    return f"{username}@{domen}"


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(0)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def unique_email():
    return generate_email()