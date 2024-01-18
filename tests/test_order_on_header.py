import pytest
from pages.order_page import OrderScooterPage


class TestOrderHeader:
    @pytest.mark.parametrize("name, surname, address, comment",[
        ("Камилла", "Габдрахманова", "г.Москва, ул.Ход.Бульвар 1", "Доставить после 19:00")
    ])
    def test_form_header(self, driver, name, surname, address, comment):
        order_scooter = OrderScooterPage(driver)
        order_scooter.go_to_site("https://qa-scooter.praktikum-services.ru/")
        order_scooter.click_button_order_header()
        order_scooter.enter_text_name(name)
        order_scooter.enter_text_surname(surname)
        order_scooter.enter_text_address(address)
        order_scooter.set_metro_station()
        order_scooter.enter_phone()
        order_scooter.click_button_next()
        order_scooter.choose_date_order()
        order_scooter.choose_rental_period()
        order_scooter.choose_date_order()
        order_scooter.enter_comment(comment)
        order_scooter.click_button_order()
        order_scooter.click_button_confirm()
        modal_text = order_scooter.get_modal_header_text()
        expected_text = "Заказ оформлен"
        assert expected_text in modal_text, f"Expected '{expected_text}' in modal header, but got: {modal_text}"





