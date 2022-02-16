import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.locators import ProductPageLocators
import time
import math


@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='Will not be debugging')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    browser.implicitly_wait(10)
    link = ('http://selenium1py.pythonanywhere.com/catalogue/'
                   'coders-at-work_207/?promo=offer{}'.format(promo_offer))
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket_from_product_page()
    page.solve_quiz_and_get_code()
    page.checking_product_added_to_basket_success()
    time.sleep(1)

