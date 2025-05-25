from selenium.webdriver.common.by import By


# Общие локаторы
class Locators:
    CREATE_ORDER = [By.XPATH,
                    "//div[contains(@class,'BurgerConstructor_basket')]/button"]  # Кнопка "Войти в аккаунт" и "Оформить заказ" на главной странице
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка "Войти" на форме регистрации и восстановлении пароля
    PERSONAL_ACCOUNT = [By.XPATH, "//p[text()='Личный Кабинет']/.."]  # Кнопка "Личный кабинет" на главной странице
    LOGO = [By.CSS_SELECTOR, "[class*='AppHeader_header__logo']"]  # Кнопка-логитип "Stellar Burger"
    CONSTRUCTOR = [By.XPATH, "//p[text()='Конструктор']/.."]  # Кнопка "Конструктор"


# Страница Войти
class Login:
    EMAIL = [By.XPATH, "//label[text()='Email']/../input"]  # Поле ввода "Email"
    PASSWORD = [By.XPATH, "//label[text()='Пароль']/../input"]  # Поле ввода "Пароль"
    AUTH_BUTTON = [By.XPATH, "//button[text()='Войти']"]  # Кнопка "Войти"
    REG_LINK = [By.XPATH, "//a[text()='Зарегистрироваться']"]  # Ссылка "Зарегистрироваться"


# Страница Регистрация
class SignUp:
    NAME = (By.XPATH, "//label[text()='Имя']/../input")  # Поле ввода "Имя"
    EMAIL = [By.XPATH, "//label[text()='Email']/../input"]  # Поле ввода "Email"
    PASSWORD = [By.XPATH, "//label[text()='Пароль']/../input"]  # Поле ввода "Пароль"
    PASSWORD_EXCEPTION = [By.XPATH,
                          "//p[text()='Некорректный пароль']"]  # Ошибка при вводе пароля менее допустимой длины
    REGISTER = [By.XPATH, "//button[text()='Зарегистрироваться']"]  # Кнопка "Зарегистрироваться"


# Страница личного кабинета
class Personal:
    QUIT_BUTTON = [By.XPATH, "//button[text()='Выход']"]  # Кнопка "Выйти"


# Форма конструктор
class Constructor:
    BUN_BUTTON = [By.XPATH, "//span[text()='Булки']"]  # Кнопка "Булки"
    SAUSE_BUTTON = [By.XPATH, "//span[text()='Соусы']"]  # Кнопка "Соусы"
    FILL_BUTTON = [By.XPATH, "//span[text()='Начинки']"]  # Кнопка "Начинки"
    BUN_SECTION = [By.XPATH, "//h2[text()='Булки']"]  # Раздел "Булки"
    SAUSE_SECTION = [By.XPATH, "//h2[text()='Соусы']"]  # Раздел "Соусы"
    FILL_SECTION = [By.XPATH, "//h2[text()='Начинки']"]  # Раздел "Начинки"
