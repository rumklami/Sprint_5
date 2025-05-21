from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from data import timeout
from helper import *
from locators import Locators, SignUp, Login
from curl import main_site, registration, auth_link, forgot_password
from conftest import driver


# Тесты на проверку регистрации и авторизации
class TestUserRegistration:

    # Проверка регистрации: 1 - успешная регистрация с заполнением всех полей,
    #                       2 - неуспешная регистрация, пропуск заполнения поля Email
    #                       3 - неуспешная регистрация, пропуск заполнения поля Имя
    @pytest.mark.parametrize("name, email, password, wait_button, expect_link",
                             [(generate_registration_name(), generate_registration_email(),
                               generate_registration_password(), Login.AUTH_BUTTON, auth_link),  # 1
                              (generate_registration_name(), '', generate_registration_password(), SignUp.NAME,
                               registration),  # 2
                              ('', generate_registration_email(), generate_registration_password(), SignUp.NAME,
                               registration)  # 3
                              ])
    def test_registration_validation(self, driver, name, email, password, wait_button, expect_link):
        # Открытие страницы Зарегистрироваться
        driver.get(registration)
        # Заполнение полей и нажатие кнопки Зарегистрироваться
        driver.find_element(*SignUp.NAME).send_keys(name)
        driver.find_element(*SignUp.EMAIL).send_keys(email)
        driver.find_element(*SignUp.PASSWORD).send_keys(password)
        driver.find_element(*SignUp.REGISTER).click()
        # Ожидание загрузки страницы
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(wait_button))
        # Проверка корректности ссылки в зависимости от заполненных полей
        assert driver.current_url == expect_link

    # Проверка вывода ошибки при вводе короткого пароля
    def test_short_pass_registration(self, driver):
        # Открытие страницы Зарегистрироваться
        driver.get(registration)
        # Заполнение обязательных полей и пароля в 4 символа, нажатие кнопки Зарегистрироваться
        driver.find_element(*SignUp.NAME).send_keys(generate_registration_name())
        driver.find_element(*SignUp.EMAIL).send_keys(generate_registration_email())
        driver.find_element(*SignUp.PASSWORD).send_keys(generate_registration_password(len=4))
        driver.find_element(*SignUp.REGISTER).click()
        # Проверка отображения текста ошибки "Некорректный пароль"
        error_text = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(SignUp.PASSWORD_EXCEPTION)).text
        assert error_text == "Некорректный пароль"

    # Проверка открытия формы входа по кнопке «Войти» на главной, через ЛК, в форме регистрации, через форму восстановления
    @pytest.mark.parametrize("website, button", [(main_site, Locators.CREATE_ORDER),
                                                 (main_site, Locators.PERSONAL_ACCOUNT),
                                                 (registration, Locators.LOGIN_LINK),
                                                 (forgot_password, Locators.LOGIN_LINK)])
    def test_login_from_main_page(self, driver, website, button):
        # Открытие страницы
        driver.get(website)
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(Locators.LOGO))
        # Нажатие на кнопку
        driver.find_element(*button).click()
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(Login.EMAIL))
        # Проверка перехода на главную страницу и проверка наличия кнопки "Оформить заказ"
        assert driver.current_url == auth_link
