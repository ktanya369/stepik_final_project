from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_SEE_BASKET = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner")
    PRODUCT_TO_BASKET = (By.CSS_SELECTOR, "h2.col-sm-6.h3")

class LoginPageLocators():
    FORM_REG = (By.CSS_SELECTOR, "#register_form")
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    REG_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_FORM_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")