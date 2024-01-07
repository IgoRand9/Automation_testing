import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_order import Finish_order
from pages.main_page import Main_page
import datetime

def test_buy_product():
    patch = 'C:\\Users\\holya\pythonProject\\resourse\\chromedriver.exe'
    g = Service(patch)
    driver = webdriver.Chrome(service=g)

    print("Start test")

    first_page = Main_page(driver) # создаём новую переменную в которую помещаем экземпляр класса Main page и передаём драйвер
    first_page.select_product()  # обращаемся к переменной и вызываем метод выбора продукта

    cp = Cart_page(driver)
    cp.product_confirmation()

    cip = Client_information_page(driver)
    cip.input_information()

    f = Finish_order(driver)
    f.finish()







    time.sleep(10)




 # python -m pytest -s -v

