from .base_page import BasePage
from .locators import GoogleSearch


class Search_website(BasePage):

    def open_mail_yandex(self):
        search = self.browser.find_element(*GoogleSearch.search_input)
        search.send_keys('Яндекс Почта')
        self.browser.find_element(*GoogleSearch.button_search).click()
        self.browser.find_element_by_partial_link_text('Яндекс.Почта').click()
        assert "mail.yandex.ru" in self.browser.current_url, 'некорректный URL'


