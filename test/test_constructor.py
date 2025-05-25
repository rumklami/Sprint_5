from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from data import timeout
from locators import Constructor
from curl import main_site
from conftest import driver


# Тесты формы Конструктора
class TestConstructor:

    # Проверка переключения разделов на форме Конструктора
    @pytest.mark.parametrize("section_start, button, expected_section",
                             [(Constructor.FILL_SECTION, Constructor.BUN_BUTTON, Constructor.BUN_SECTION),
                              (Constructor.BUN_SECTION, Constructor.SAUSE_BUTTON, Constructor.SAUSE_SECTION),
                              (Constructor.BUN_SECTION, Constructor.FILL_BUTTON, Constructor.FILL_SECTION)])
    def test_switch_section_constructor(self, driver, section_start, button, expected_section):
        # Открытие главной страницы
        driver.get(main_site)
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(button))
        # Скролл до раздела, отличного от проверяемого раздела
        driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(*section_start))
        # Нажатие на кнопку переключения раздела
        driver.find_element(*button).click()
        assert EC.visibility_of_element_located(expected_section)
