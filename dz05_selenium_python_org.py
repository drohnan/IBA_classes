import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        # открытие в Firefox страницы http://www.python.org
        driver.get("http://www.python.org")
        # проверка наличия слова Python в заголовке страницы
        self.assertIn("Python", driver.title)
        # ждем 5 секунд
        time.sleep(5)
        # получение элемента страницы с именем q (строка поиска)
        # (откройте вручную в любом браузере сайт http://www.python.org,
        # нажмите правой кнопкой мыши по строке поиска,
        # выберите пункт "просмотреть код",
        # убедитесь, что у этого элемента name="q")
        elem = driver.find_element_by_name("q")
        # ждем 5 секунд
        time.sleep(5)
        # набор слова chupakabra в найденном элементе
        elem.send_keys("chupakabra")
        # ждем 5 секунд
        time.sleep(5)
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(5)
        # проверка наличия строки "No results found."
        # на странице с результатами поиска
        self.assertIn("No results found.", driver.page_source)
        # ждем 5 секунд
        time.sleep(5)
        # получение элемента страницы с именем q
        # на обновленной странице
        elem = driver.find_element_by_name("q")
        # очищаем строку поиска
        elem.clear()
        # ждем 5 секунд
        time.sleep(5)
        # набор слова pycon в найденном элементе
        elem.send_keys("pycon")
        # ждем 5 секунд
        time.sleep(5)
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(5)
        # проверка отсутствия строки "No results found."
        # на странице с результатами поиска
        self.assertNotIn("No results found.", driver.page_source)

    def test_login_logout(self):
        driver = self.driver
        # открытие в Firefox страницы http://www.python.org/psf-landing/
        # на которой есть кнопка Sign In
        driver.get("https://www.python.org/psf-landing/")
        # ждем 5 секунд
        time.sleep(5)
        # поиск ссылки с текстом "Sign In"
        elem = driver.find_element_by_link_text("Sign In")
        # нажатие на ссылку
        elem.click()
        # ждем 5 секунд
        time.sleep(5)
        # поиск текстового поля для ввода логина по XPath
        # (тег input с name='login')
        elem = driver.find_element_by_xpath("//input[@name='login']")
        # ввод логина
        elem.send_keys("drohnan")
        # ждем 5 секунд
        time.sleep(5)
        # поиск текстового поля для ввода пароля по XPath
        # (тег input с name='password')
        elem = driver.find_element_by_xpath("//input[@name='password']")
        # ввод логина
        elem.send_keys("19Flac99")
        # ждем 5 секунд
        time.sleep(5)
        # жмем ввод для отправки формы
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(5)
        # проверка наличия на странице строки "Your account"
        # после входа
        self.assertIn("Your account", driver.page_source)
        # ждем 5 секунд
        time.sleep(5)
        # вывод кода страницы для отладки, потом можно будет убрать
        print(driver.page_source)
        # поиск ссылки с текстом "Sign out"
        # elem = driver.find_element_by_link_text("Sign out")
        # # нажатие на ссылку
        # elem.click()
        driver.get("https://www.python.org/accounts/logout/")
        # ждем 5 секунд
        time.sleep(5)
        # поиск кнопки на форме в главной области страницы
        # по CSS-селектору
        elem = driver.find_element_by_css_selector(
            'div.container section.main-content form button'
        )  # нажатие на кнопку
        elem.click()
        # ждем 5 секунд
        time.sleep(5)
        # проверка отсутствия на странице строки "Your account"
        # после выхода
        self.assertNotIn("Your account", driver.page_source)

    def test_quotes_links(self):
        driver = self.driver
        driver.get("https://www.python.org")
        time.sleep(5)
        # Кнопка About/Quotes
        about_link = driver.find_element(By.LINK_TEXT, "Quotes")
        about_link.click()
        time.sleep(5)
        # ссылка на YouTube.com
        youtube_link = driver.find_element(By.LINK_TEXT, "YouTube.com")
        youtube_link.click()
        time.sleep(5)

    def test_irc_links(self):
        driver = self.driver
        driver.get("https://www.python.org")
        time.sleep(5)
        # Кнопка Community/IRC
        irc_link = driver.find_element(By.LINK_TEXT, "irc") # зафейлится, потому что текст большими буквами IRC на ссылке
        irc_link.click()
        time.sleep(5)

    def test_donate(self):
        driver = self.driver
        driver.get("https://www.python.org")
        time.sleep(5)
        # кнопка Donate
        donate_button = driver.find_element(By.CLASS_NAME, "donate-button")
        donate_button.click()
        time.sleep(5)
        # перебираем радиобатоны, чтобы красиво кружочки нажимались :)
        driver.find_element(By.XPATH, '//*[@id="CIVICRM_QFID_19_4"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="CIVICRM_QFID_20_6"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="CIVICRM_QFID_21_8"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="CIVICRM_QFID_22_10"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="CIVICRM_QFID_23_12"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="CIVICRM_QFID_139_14"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="CIVICRM_QFID_140_16"]').click()
        time.sleep(2)
        other_amount_radio_btn = driver.find_element(By.XPATH, '//*[@id="priceset"]/div[1]/div[2]/div[8]/span')
        other_amount_radio_btn.click()
        time.sleep(2)
        # ввод значения в other amount
        driver.find_element(By.XPATH, '//*[@id="price_47"]').send_keys("42.56")
        time.sleep(2)
        # Тыкаем чекбокс I want to contribute this amount every
        driver.find_element(By.XPATH, '//*[@id="is_recur"]').click()
        time.sleep(2)
        # в комбобоксе выбираем "year"
        driver.find_element(By.XPATH, '//*[@id="frequency_unit"]/option[2]').click()
        time.sleep(2)
        # в instalments эдитбокс знаечение
        driver.find_element(By.XPATH, '//*[@id="installments"]').send_keys("2")
        time.sleep(2)
        #  и так далее... :)


    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
