from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button.click()

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_BASKET), "Button add to basket is not presented"

    def should_be_correct_add_product(self):
        self.should_be_success_message()
        self.should_be_correct_product()
        self.should_be_correct_price()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def should_be_correct_product(self):
        name_product_on_site = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        name_product_on_site_text = name_product_on_site.text
        name_product_to_basket = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        name_product_to_basket_text = name_product_to_basket.text
        assert name_product_on_site_text == name_product_to_basket_text, "Name book is different"
    
    def should_be_correct_price(self):
        price_product_on_site = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        price_product_on_site_text = price_product_on_site.text
        price_product_to_basket = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE)
        price_product_to_basket_text = price_product_to_basket.text
        assert price_product_on_site_text == price_product_to_basket_text, "Price book is different"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    
    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"