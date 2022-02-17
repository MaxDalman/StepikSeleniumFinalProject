from selenium.webdriver.common.by import By
from .base_page import BasePage


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_ADDED = (By.CLASS_NAME, "alert-info")
    
    PRODUCT_PAGE_NAME = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/h1")
    PRODUCT_ADDED_SUCCESS = (By.XPATH, "//div[@id='messages']/div/div/strong")

    MESSAGE_SUCCESS = (By.CSS_SELECTOR, '.alertinner')
