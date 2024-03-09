import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_managment():
    browser.config.base_url="https://demoqa.com/automation-practice-form"

    yield

    browser.quit()
