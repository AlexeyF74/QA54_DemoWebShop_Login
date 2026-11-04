# Импортируем Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Класс для негативных тестов авторизации
class TestNegativeLogin:

    # Выполняется перед каждым тестом
    def setup_method(self):
        # Открываем браузер Chrome
        self.driver = webdriver.Chrome()

        # Ожидание появления элементов до 15 секунд
        self.wait = WebDriverWait(self.driver, 15)

    # Выполняется после каждого теста
    def teardown_method(self):
        # Закрываем браузер
        self.driver.quit()

    # ТЕСТ 1: Незарегистрированный Email
    def test_login_with_unregistered_email(self):

        # Открываем сайт
        self.driver.get("https://demowebshop.tricentis.com/")

        # Нажимаем Log in
        self.driver.find_element(By.LINK_TEXT, "Log in").click()

        # Вводим незарегистрированный Email
        self.driver.find_element(By.ID, "Email").send_keys(
            "notregistered123@example.com"
        )

        # Вводим пароль
        self.driver.find_element(By.ID, "Password").send_keys(
            "TestPassword123!"
        )

        # Нажимаем Login
        self.driver.find_element(
            By.CSS_SELECTOR, "input.button-1.login-button"
        ).click()

        # Ожидаем сообщение об ошибке
        error = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".validation-summary-errors")
            )
        )

        # Проверяем результат
        assert "No customer account found" in error.text

    # ТЕСТ 2: Зарегистрированный Email и неправильный Password
    def test_login_with_wrong_password(self):

        # Открываем сайт
        self.driver.get("https://demowebshop.tricentis.com/")

        # Нажимаем Log in
        self.driver.find_element(By.LINK_TEXT, "Log in").click()

        # Вводим зарегистрированный Email
        self.driver.find_element(By.ID, "Email").send_keys(
            "YOUR_REGISTERED_EMAIL@example.com"
        )

        # Вводим неправильный пароль
        self.driver.find_element(By.ID, "Password").send_keys(
            "WrongPassword123"
        )

        # Нажимаем Login
        self.driver.find_element(
            By.CSS_SELECTOR, "input.button-1.login-button"
        ).click()

        # Ожидаем сообщение об ошибке
        error = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".validation-summary-errors")
            )
        )

        # Проверяем, что авторизация отклонена
        assert error.is_displayed()
        assert "unsuccessful" in error.text.lower()

    # ТЕСТ 3: Пустой Password
    def test_login_with_empty_password(self):

        # Открываем сайт
        self.driver.get("https://demowebshop.tricentis.com/")

        # Нажимаем Log in
        self.driver.find_element(By.LINK_TEXT, "Log in").click()

        # Вводим зарегистрированный Email
        self.driver.find_element(By.ID, "Email").send_keys(
            "YOUR_REGISTERED_EMAIL@example.com"
        )

        # Поле Password оставляем пустым

        # Нажимаем Login
        self.driver.find_element(
            By.CSS_SELECTOR, "input.button-1.login-button"
        ).click()

        # Проверяем, что браузер или сайт отклонил пустой пароль
        password_input = self.driver.find_element(By.ID, "Password")

        password_is_required = self.driver.execute_script(
            "return arguments[0].validity.valueMissing;",
            password_input
        )

        if password_is_required:
            assert password_is_required
        else:
            error = self.wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".validation-summary-errors")
                )
            )

            assert error.is_displayed()
            assert error.text.strip() != ""
