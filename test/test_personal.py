from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from data import timeout
from locators import Locators, Login, Personal
from curl import main_site, auth_link, personal_account
from conftest import authorization


# Тесты на странице Личного кабинета
class TestPersonalAccount:

    # Проверка перехода в Личный кабинет
    def test_open_order_page(self, authorization):
        # Выполнение авторизации и переход в Личный кабинет
        authorization.find_element(*Locators.PERSONAL_ACCOUNT).click()
        # Ожидание загрузки страницы
        WebDriverWait(authorization, timeout).until(EC.visibility_of_element_located(Personal.QUIT_BUTTON))
        # Проверка ссылки отображаемой страницы
        assert authorization.current_url == personal_account

    # Проверка перехода из ЛК: 1 - в конструктор
    #                          2 - на логотип Stellar Burgers
    #                          3 - Выход из ЛК
    @pytest.mark.parametrize("button, wait_field, expect_link",
                             [(Locators.CONSTRUCTOR, Locators.CREATE_ORDER, main_site),  # 1
                              (Locators.LOGO, Locators.CREATE_ORDER, main_site),  # 2
                              (Personal.QUIT_BUTTON, Login.EMAIL, auth_link)])  # 3
    def test_navigate_to_main_from_personal_account(self, authorization, button, wait_field, expect_link):
        # Выполнение авторизации и переход в Личный кабинет
        authorization.find_element(*Locators.PERSONAL_ACCOUNT).click()
        # Ожидание загрузки страницы
        WebDriverWait(authorization, timeout).until(EC.visibility_of_element_located(button))
        # Нажатие на кнопку и ожидание загрузки страницы
        authorization.find_element(*button).click()
        WebDriverWait(authorization, timeout).until(EC.visibility_of_element_located(wait_field))
        # Проверка ссылки отображаемой главной страницы
        assert authorization.current_url == expect_link
