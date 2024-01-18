import time

import allure
import pytest

from asserts.base_assert import Asserts
from locators.main_page_locators import FAQLocators
from pages.main_page import YaMainPage


class TestTextQuestion:
    @allure.feature('Проверка текста в блоке FAQ на соответствие введенному нами тексту')
    @allure.title('Проверка текста в блоке "Вопрос"')
    @allure.description('Сравниваем текст в каждом заголовке "Вопрос" с ожидаемым текстом')
    @allure.step('Сравниваем каждый заголовок текста в блоке "Вопрос"')
    @pytest.mark.parametrize(("text", "locator"),
                            [
                                ("Сколько это стоит? И как оплатить?",
                                 FAQLocators.FAQ_QUESTION_1),
                                ("Хочу сразу несколько самокатов! Так можно?",
                                 FAQLocators.FAQ_QUESTION_2),
                                ("Как рассчитывается время аренды?",
                                 FAQLocators.FAQ_QUESTION_3),
                                ("Можно ли заказать самокат прямо на сегодня?",
                                 FAQLocators.FAQ_QUESTION_4),
                                ("Можно ли продлить заказ или вернуть самокат раньше?",
                                 FAQLocators.FAQ_QUESTION_5),
                                ("Вы привозите зарядку вместе с самокатом?",
                                 FAQLocators.FAQ_QUESTION_6),
                                ("Можно ли отменить заказ?",
                                 FAQLocators.FAQ_QUESTION_7),
                                ("Я жизу за МКАДом, привезёте?",
                                 FAQLocators.FAQ_QUESTION_8),
                            ])
    def test_faq_question(self, driver, text, locator):
        ya_main_page = YaMainPage(driver)
        asserts_instance = Asserts(driver)
        ya_main_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        ya_main_page.scroll_page_down()
        question_element = driver.find_element(*locator)
        driver.execute_script("arguments[0].scrollIntoView(true);", question_element)
        time.sleep(1)
        locator_type, locator_value = locator
        assert asserts_instance.text_is_correct(text, (locator_type, locator_value))