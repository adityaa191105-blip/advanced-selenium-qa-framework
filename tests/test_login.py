from pages.login_page import LoginPage

class TestLogin:

    def test_login_valid(self, driver):

        page = LoginPage(driver)

        page.login(
            'standard_user',
            'secret_sauce'
        )

        assert 'inventory' in driver.current_url

    def test_login_invalid(self, driver):

        page = LoginPage(driver)

        page.login(
            'wrong_user',
            'wrong_password'
        )

        assert page.is_login_failed()