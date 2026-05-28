from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class LoginPage(BasePage):

    URL = 'https://www.saucedemo.com/'

    USERNAME = (
        By.ID,
        'user-name'
    )

    PASSWORD = (
        By.ID,
        'password'
    )

    LOGIN_BUTTON = (
        By.ID,
        'login-button'
    )

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        'h3[data-test="error"]'
    )

    def navigate(self):

        self.open(self.URL)

    def login(self, username, password):

        self.navigate()

        self.type(
            self.USERNAME,
            username
        )

        self.type(
            self.PASSWORD,
            password
        )

        self.click(
            self.LOGIN_BUTTON
        )

    def is_login_failed(self):

        return self.is_visible(
            self.ERROR_MESSAGE
        )