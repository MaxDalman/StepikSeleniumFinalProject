from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_product_to_basket_from_product_page(self):
        btn_add_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        btn_add_basket.click()
        

    def checking_product_added_to_basket_success(self):
        # Проверяем, что товар добавился в корзину
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED), "Product is not added to basket"

        # Проверяем, что название товара совпадает с добавленным в корзину
        name_product_added = self.browser.find_element_by_xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1')
        message_product_added_success = self.browser.find_element_by_xpath('//*[@id="messages"]/div[1]/div/strong')
        print(name_product_added.text)
        print(message_product_added_success.text)
        assert name_product_added.text == message_product_added_success.text, "Wrong product added to cart"

        # Проверяем на соответствие цены выбранного товара с товаром в корзине
        price_product_added = self.browser.find_element_by_css_selector('#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color') 
        price_product_added_success = self.browser.find_element_by_css_selector('#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
        print(price_product_added.text)
        print(price_product_added_success.text)
        assert price_product_added.text == price_product_added_success.text, "Wrong price in the cart"

        # # Проверяем, что находимся на странице с промо
        # assert "promo=newYear" in self.url, "'newYear' not in current url"