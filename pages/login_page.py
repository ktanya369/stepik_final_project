from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url, "Url is good"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "Login form is presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.FORM_REG), "Register form is presented"

    def register_new_user(self, email, password):
        input_reg_email = self.browser.find_element(*LoginPageLocators.REG_FORM_EMAIL)
        input_reg_email.send_keys(email)
        input_reg_password1 = self.browser.find_element(*LoginPageLocators.REG_FORM_PASSWORD)
        input_reg_password1.send_keys(password)
        input_reg_password2 = self.browser.find_element(*LoginPageLocators.REG_FORM_REPEAT_PASSWORD)
        input_reg_password2.send_keys(password)
        button_reg = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        button_reg.click()