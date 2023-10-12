from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datatest import nameForRegistration, emailForRegistrtion, passwordForRegistration, incorrectPasswordForRegistration
from locators import *

class TestRegistration:
    def test_reginstration_with_valid_password(self, driver):
        driver.find_element(By.XPATH, loginButton).click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, enterLink)))

        driver.find_element(By.LINK_TEXT, 'Зарегистрироваться').click()

        driver.find_element(By.XPATH, registrationNameField).send_keys(nameForRegistration)
        driver.find_element(By.XPATH, registrationEmailField).send_keys(emailForRegistrtion)
        driver.find_element(By.XPATH, registrationPasswordField).send_keys(passwordForRegistration)

        driver.find_element(By.XPATH, registerButton).click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, enterLink)))

        assert "login" in driver.current_url

    def test_reginstration_with_invalid_password(self, driver):
        driver.find_element(By.XPATH, loginButton).click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, enterLink)))

        driver.find_element(By.LINK_TEXT, 'Зарегистрироваться').click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, registrationLink)))

        driver.find_element(By.XPATH, registrationNameField).send_keys(nameForRegistration)
        driver.find_element(By.XPATH, registrationEmailField).send_keys(emailForRegistrtion)
        driver.find_element(By.XPATH, registrationPasswordField).send_keys(incorrectPasswordForRegistration)

        driver.find_element(By.XPATH, registerButton).click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, incorrectPasswordText)))

        assert driver.find_element(By.XPATH, incorrectPasswordText).text == "Некорректный пароль"
