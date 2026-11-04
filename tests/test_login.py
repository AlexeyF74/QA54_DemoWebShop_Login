from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 15)

    def teardown_method(self):
        self.driver.quit()


    def test_successful_login(self):
        # 1. Открываем сайт
        self.driver.get("https://demowebshop.tricentis.com/")

        # 2. Переходим на страницу логина
        self.driver.find_element(By.LINK_TEXT, "Log in").click()

        # 3. Находим поле Email
        email_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "Email"))
        )

        # 4. Вводим email зарегистрированного пользователя
        email_input.send_keys("assfaa173@gmail.com")

        # 5. Находим поле Password
        password_input = self.driver.find_element(By.ID, "Password")

        # 6. Вводим учебный пароль
        password_input.send_keys("Aa197411")

        # 7. Нажимаем Log in
        self.driver.find_element(
            By.CSS_SELECTOR,
            "input.button-1.login-button"
        ).click()

        # 8. Проверяем успешную авторизацию
        account_link = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "a.account")
            )
        )

        assert account_link.is_displayed()
        assert account_link.text == "assfaa173@gmail.com"
        # self.wait.until(
        #     EC.visibility_of_element_located(
        #         (By.CSS_SELECTOR, "a.account")
        #     )
        # )
        #
        # assert self.driver.find_element(
        #     By.CSS_SELECTOR, "a.account"
        # ).is_displayed()