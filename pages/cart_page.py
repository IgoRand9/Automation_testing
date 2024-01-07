from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    add_in_cart = "//button[@class='e11w80q30 e4uhfkv0 app-catalog-1lk9ql2 e4mggex0']"
    go_cart = "//button[@class='e4uhfkv0 css-gh3izc e4mggex0']"
    checkout = "//button[@class='e4uhfkv0 css-ch34l1 e4mggex0']"


    # Getters

    def get_add_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_in_cart)))

    def get_go_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_cart)))

    def get_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout)))


    # Actions


    def click_add_in_cart(self):
        self.get_add_in_cart().click()
        print("Click add in cart")

    def click_go_cart(self):
        self.get_go_cart().click()
        print("Click go cart")

    def click_checkout(self):
        self.get_checkout().click()
        print("Click checkout")


    # Methods


    def product_confirmation(self):
        self.click_add_in_cart()
        self.click_go_cart()
        self.click_checkout()















