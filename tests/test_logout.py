from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datatest import emailForLogin, passwordForLogin
from locators import *

class TestLogout:
    def test_logout_from_profile(self, driver):
        driver.find_element(By.XPATH, loginButton).click()

        driver.find_element(By.XPATH, emailField).send_keys(emailForLogin)
        driver.find_element(By.XPATH, passwordField).send_keys(passwordForLogin)
        driver.find_element(By.XPATH, enterButton).click()

        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, makeBurgerText)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.find_element(By.XPATH, profileButton).click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, profileLink)))

        assert "profile" in driver.current_url

        driver.find_element(By.XPATH, logoutButton).click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, enterLink)))

        assert "login" in driver.current_url










