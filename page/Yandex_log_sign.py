from .base_page import BasePage
from .locators import YandexMail

class LogInYandex(BasePage):

    def login_valid_user(self):
        self.browser.find_element(*YandexMail.main_login).click()
        self.browser.find_element(*YandexMail.email_input).send_keys('dm1try.zz')
        self.browser.find_element(*YandexMail.submit_button).click()
        self.browser.find_element(*YandexMail.password_input).send_keys('starwars')
        self.browser.find_element(*YandexMail.submit_button).click()
