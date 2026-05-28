import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():

    options = webdriver.ChromeOptions()

    options.add_argument('--start-maximized')

    if os.getenv('CI'):
        options.add_argument('--headless=new')

    service = Service(
        executable_path='chromedriver.exe'
    )

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:

        driver = item.funcargs.get('driver')

        if driver:

            os.makedirs(
                'reports/screenshots',
                exist_ok=True
            )

            name = item.nodeid.replace(
                '::',
                '_'
            ).replace(
                '/',
                '_'
            )

            driver.save_screenshot(
                f'reports/screenshots/{name}.png'
            )