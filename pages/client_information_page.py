from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Client_information_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    first_name = "//input[@name='contact-form_firstName']"
    last_name = "//input[@name='contact-form_lastName']"
    phones = "//input[@name='contact-form_phone']"


    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phones(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phones)))





    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_phones(self, phones):
        self.get_phones().send_keys(phones)
        print("Input phones")




    # Methods



    def input_information(self):

        self.get_current_url()
        self.input_first_name("Igor")
        self.input_last_name("Andreev")
        self.input_phones("1234567890")












