from selenium.webdriver.common.by import By



class GoogleSearch:
    search_input = (By.CLASS_NAME, 'gLFyf.gsfi')
    button_search = (By.CLASS_NAME, 'gNO89b')

class YandexMail:
    main_login = (By.CLASS_NAME, 'button2.button2_size_mail-big.button2_theme_mail-white.button2_type_link.HeadBanner'
                                 '-Button.HeadBanner-Button-Enter.with-shadow')
    main_sigin = (By.CSS_SELECTOR, 'span[data-reactid="23"]')
    email_input = (By.CSS_SELECTOR, 'input[name="login"]')
    password_input = (By.CSS_SELECTOR, 'input[name="passwd"]')
    submit_button = (By.CSS_SELECTOR, 'button[type="submit"]')
    yandex_password = (By.PARTIAL_LINK_TEXT, 'Яндекс.Паспорт')
    text_yandex_mail = (By.CSS_SELECTOR, 'table[align="center"]')

class MailSend:
    send_message = (By.CSS_SELECTOR, 'span[class="mail-ComposeButton-Text"]')
    to_whom = (By.CSS_SELECTOR, 'div[class="composeYabbles"]')
    topic = (By.CSS_SELECTOR, 'input[class="composeTextField ComposeSubject-TextField"]')
    message_window = (By.CLASS_NAME, 'cke_wysiwyg_div.cke_reset.cke_enable_context_menu.cke_editable')
    font_bold = (By.CLASS_NAME, 'cke_button.cke_button__bold.cke_button')
    font_italics = (By.CLASS_NAME, 'cke_button.cke_button__italic.cke_button')
    font_underline = (By.CLASS_NAME, 'cke_button.cke_button__underline.cke_button')
    send_read_message = (By.CLASS_NAME, 'ComposeControlPanelButton-Button_action')
    message_info = (By.CLASS_NAME, 'ComposeDoneScreen-Title')


