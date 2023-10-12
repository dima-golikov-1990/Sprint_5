from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestNavigation:
    def test_navigation_to_account(self, driver):
        driver.find_element(By.XPATH, Locators.profileButton).click()

        assert "login" in driver.current_url

    def test_navigation_from_account_to_constructor(self, driver):
        driver.find_element(By.XPATH, Locators.profileButton).click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.enterLink)))

        assert "login" in driver.current_url

        driver.find_element(By.XPATH, Locators.constructorButton).click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.makeBurgerText)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_navigation_from_account_to_constructor_use_click_logo(self, driver):
        driver.find_element(By.XPATH, Locators.profileButton).click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.enterLink)))

        assert "login" in driver.current_url

        driver.find_element(By.CLASS_NAME, Locators.StellaBurgerLogo).click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.makeBurgerText)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_navigation_tab_buns(self, driver):
        tabs = driver.find_elements(By.XPATH, Locators.tabComponents)

        driver.find_element(By.XPATH, Locators.tabsBlock).click()

        tabs[0].click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.tabAreaBuns)))

        current_scroll_position = driver.execute_script("return document.querySelector('" + Locators.tabScroll + "').scrollTop")

        assert current_scroll_position == 0

    def test_navigation_tab_sauces(self, driver):
        tabs = driver.find_elements(By.XPATH, Locators.tabComponents)

        driver.find_element(By.XPATH, Locators.tabsBlock).click()

        tabs[0].click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.tabAreaBuns)))

        current_scroll_position = driver.execute_script("return document.querySelector('" + Locators.tabScroll + "').scrollTop")
        old_scroll_position = current_scroll_position

        tabs[1].click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.tabAreaSauces)))

        current_scroll_position = driver.execute_script("return document.querySelector('" + Locators.tabScroll + "').scrollTop")

        assert current_scroll_position != old_scroll_position


    def test_navigation_tab_fillings(self, driver):
        tabs = driver.find_elements(By.XPATH, Locators.tabComponents)

        driver.find_element(By.XPATH, Locators.tabsBlock).click()

        tabs[0].click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.tabAreaBuns)))

        current_scroll_position = driver.execute_script("return document.querySelector('" + Locators.tabScroll + "').scrollTop")
        old_scroll_position = current_scroll_position

        tabs[2].click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, Locators.tabAreaFillings)))

        current_scroll_position = driver.execute_script("return document.querySelector('" + Locators.tabScroll + "').scrollTop")

        assert current_scroll_position != old_scroll_position
