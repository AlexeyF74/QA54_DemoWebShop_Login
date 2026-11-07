
import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:

    def setup_method(self):
        # Открываем новый браузер без активной сессии
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 15)

    def teardown_method(self):
        # Закрываем браузер после теста
        self.driver.quit()

    def test_successful_registration(self):

        # Получаем пароль из переменной окружения
        password = os.getenv("DEMO_SHOP_PASSWORD")
        assert password, "Set DEMO_SHOP_PASSWORD before running the test"

        # Создаём уникальный email для каждой регистрации
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        email = f"qa.registration.{timestamp}@example.com"

        # Открываем сайт
        self.driver.get("https://demowebshop.tricentis.com/")

        # Нажимаем Register
        self.wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Register")
            )
        ).click()

        # Заполняем First name
        self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "FirstName")
            )
        ).send_keys("Alex")

        # Заполняем Last name
        self.driver.find_element(
            By.ID, "LastName"
        ).send_keys("Tester")

        # Заполняем Email
        self.driver.find_element(
            By.ID, "Email"
        ).send_keys(email)

        # Заполняем Password
        self.driver.find_element(
            By.ID, "Password"
        ).send_keys(password)

        # Заполняем Confirm password
        self.driver.find_element(
            By.ID, "ConfirmPassword"
        ).send_keys(password)

        # Нажимаем Register
        self.driver.find_element(
            By.ID, "register-button"
        ).click()

        # Ожидаем подтверждение регистрации
        result = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "result")
            )
        )

        # Выводим точный текст подтверждения
        print("Registration result:", result.text)

        # Проверяем успешную регистрацию
        assert "Your registration completed" in result.text

        # Сохраняем скриншот успешного результата
        self.driver.save_screenshot("registration_success.png")
