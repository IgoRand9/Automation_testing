from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):   # передаём класс base в main_page

    url = 'https://www.citilink.ru/'

    def __init__(self, driver):
        super().__init__(driver) # указывает на потомок класса
        self.driver = driver

    # Locators

    catalog = "//a[@class=' css-15x7smt enj50b10']"
    laptops = "//div[@class='app-catalog-rtud02 e13gmytb0']"
    phones_gadgets = "/html/body/div[7]/div/div/div/div/div[2]/div/div/div/div[5]/div/div/div/div/div[1]/div/div/div/div/div/div[1]/div/a[1]/div/span"
    phones = "//span[@class='app-catalog-pt72uc e66p2eb0']"
    huawei = "//a[@title='Смартфон Huawei P60 Pro 8/256Gb,  MNA-LX9,  черный']"



    # Getters

    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_laptops(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.laptops)))

    def get_phones_gadgets(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phones_gadgets)))

    def get_phones(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phones)))

    def get_huawei(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.huawei)))




    # Actions

    def click_catalog(self):
        self.get_catalog().click()
        print("Click enter catalog")

    def click_laptops(self):
        self.get_laptops().click()
        print("Click laptops")

    def click_phones_gadgets(self):
        self.get_phones_gadgets().click()
        print("Click phones gadgets")

    def click_phones(self):
        self.get_phones().click()
        print("Click phones")


    def click_huawei(self):
        self.get_huawei().click()
        print("Click huawei")



    # Methods



    def select_product(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_catalog()
        self.click_phones_gadgets()
        self.click_phones()
        self.click_huawei()














