from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datatest import emailForLogin, passwordForLogin
from locators import Locators

class TestLogin:
    def test_login_using_the_login_to_account_button(self, driver):
        driver.find_element(By.XPATH, Locators.loginButton).click()

        driver.find_element(By.XPATH, Locators.emailField).send_keys(emailForLogin)
        driver.find_element(By.XPATH, Locators.passwordField).send_keys(passwordForLogin)
        driver.find_element(By.XPATH, Locators.enterButton).click()

        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.makeBurgerText)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_using_the_account_button(self, driver):
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.makeBurgerText)))

        driver.find_element(By.XPATH, Locators.profileButton).click()

        driver.find_element(By.XPATH, Locators.emailField).send_keys(emailForLogin)
        driver.find_element(By.XPATH, Locators.passwordField).send_keys(passwordForLogin)
        driver.find_element(By.XPATH, Locators.enterButton).click()

        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.makeBurgerText)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_in_registration_page(self, driver):
        driver.find_element(By.XPATH, Locators.loginButton).click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.enterLink)))

        driver.find_element(By.LINK_TEXT, 'Зарегистрироваться').click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.registrationLink)))

        driver.find_element(By.LINK_TEXT, 'Войти').click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.enterLink)))

        driver.find_element(By.XPATH, Locators.emailField).send_keys(emailForLogin)
        driver.find_element(By.XPATH, Locators.passwordField).send_keys(passwordForLogin)
        driver.find_element(By.XPATH, Locators.enterButton).click()

        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.makeBurgerText)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_login_in_recover_password_page(self, driver):
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.enterLink)))

        driver.find_element(By.LINK_TEXT, 'Восстановить пароль').click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.recoverPasswordLink)))

        driver.find_element(By.LINK_TEXT, 'Войти').click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.enterLink)))

        driver.find_element(By.XPATH, Locators.emailField).send_keys(emailForLogin)
        driver.find_element(By.XPATH, Locators.passwordField).send_keys(passwordForLogin)
        driver.find_element(By.XPATH, Locators.enterButton).click()

        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.makeBurgerText)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
