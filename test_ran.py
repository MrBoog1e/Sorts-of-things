from .page.Google_search import Search_website
from .page.Yandex_log_sign import LogInYandex
from .page.MailLogic import VerificationMail
import pytest
import time

link = 'https://www.google.com/'
link1 = 'https://mail.yandex.ru/'


class Test_1:
    def test_search_yandex_mail(self, browser):
        page = Search_website(browser, link)
        page.open()
        page.open_mail_yandex()
        page = LogInYandex(browser, link)
        page.login_valid_user()

    def test_verification_sample_mail(self, browser):
        page = Search_website(browser, link)
        page.open()
        page.open_mail_yandex()
        page = LogInYandex(browser, link)
        page.login_valid_user()
        page = VerificationMail(browser, link)
        page.verification_yandex_password()

    @pytest.mark.d1
    def test_message_send(self, browser):
        page = LogInYandex(browser, link1)
        page.open()
        page.login_valid_user()
        page = VerificationMail(browser, link1)
        page.alert()
        page.send_message()
