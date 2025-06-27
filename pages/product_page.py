from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button.click()
        #alert = self.browser.switch_to.alert
        #alert.accept()
    
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_BASKET), "Button add to basket is not presented"