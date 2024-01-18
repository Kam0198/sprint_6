from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_STATUS_BUTTON = (By.XPATH, "//button[contains(text(),'Статус заказа')]")
    ORDER_BUTTON_HEADER = (By.CSS_SELECTOR, "[class*='Header_Nav__AGCXC'] [class*='Button_Button__ra12g']")
    ORDER_BUTTON_MIDDLE = (By.XPATH, "//div/div[5]/button[text()='Заказать']")

    LOGO_SCOOTER = (By.CSS_SELECTOR, "[class*='Header_Logo'] [alt='Scooter']")
    LOGO_YANDEX = (By.CSS_SELECTOR, "[class*='Header_Logo'] [alt='Yandex']")


class FAQLocators:
    FAQ_BLOCK = (By.CLASS_NAME, "[class='accordion']")
    FAQ_QUESTION_1 = (By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-0"]')
    FAQ_ANSWER_1 = (By.CSS_SELECTOR, '[id="accordion__panel-0"] > p')
    FAQ_QUESTION_2 = (By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-1"]')
    FAQ_ANSWER_2 = (By.CSS_SELECTOR, '[id="accordion__panel-1"] > p')
    FAQ_QUESTION_3 = (By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-2"]')
    FAQ_ANSWER_3 = (By.CSS_SELECTOR, '[id="accordion__panel-2"] > p')
    FAQ_QUESTION_4 = (By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-3"]')
    FAQ_ANSWER_4 = (By.CSS_SELECTOR, '[id="accordion__panel-3"] > p')
    FAQ_QUESTION_5 = (By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-4"]')
    FAQ_ANSWER_5 = (By.CSS_SELECTOR, '[id="accordion__panel-4"] > p')
    FAQ_QUESTION_6 = (By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-5"]')
    FAQ_ANSWER_6 = (By.CSS_SELECTOR, '[id="accordion__panel-5"] > p')
    FAQ_QUESTION_7 = (By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-6"]')
    FAQ_ANSWER_7 = (By.CSS_SELECTOR, '[id="accordion__panel-6"] > p')
    FAQ_QUESTION_8 = (By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-7"]')
    FAQ_ANSWER_8 = (By.CSS_SELECTOR, '[id="accordion__panel-7"] > p')

