from .base_page import BasePage
from .locators import YandexMail, MailSend
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException


class VerificationMail(BasePage):

    def alert(self):
        try:
            self.browser.switch_to.alert.accept()
        except NoAlertPresentException:
            print("no alert")

    def verification_yandex_password(self):
        self.browser.find_element(*YandexMail.yandex_password).click()
        text_mail = self.browser.find_element(*YandexMail.text_yandex_mail).text
        assert 'ДМИТРИЙ' and 'dm1try.zz' in text_mail, 'ERROR: No user message'

    def send_message(self):
        self.browser.find_element(*MailSend.send_message).click()
        self.browser.find_element(*MailSend.to_whom).send_keys('mrboog1e@ya.ru')
        self.browser.find_element(*MailSend.topic).send_keys('Проверка')
        self.browser.find_element(*MailSend.font_bold).click()
        self.browser.find_element(*MailSend.message_window).send_keys('Проверка шрифта1', Keys.ENTER)
        self.browser.find_element(*MailSend.font_italics).click()
        self.browser.find_element(*MailSend.message_window).send_keys('Проверка шрифта2', Keys.ENTER)
        self.browser.find_element(*MailSend.font_underline).click()
        self.browser.find_element(*MailSend.message_window).send_keys('Проверка шрифта3', Keys.ENTER)
        self.browser.find_element(*MailSend.send_read_message).click()
        assert self.browser.find_element(*MailSend.message_info), ('ERROR SCREEN1', self.browser.get_screenshot_as_file(
            filename='screen1'))
