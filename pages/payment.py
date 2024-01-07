from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Payment(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

    accept_order = "//button[@id='finish']"

    # Getters

    def get_accept_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accept_order)))

    # Actions

    def click_accept_order(self):
        self.get_accept_order().click()
        print("Click accept order")

    # Methods

    def payment(self):
        self.get_current_url()
        self.click_accept_order()













