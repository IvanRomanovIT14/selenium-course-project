from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        add_button.click()

    def get_product_name(self):
        """Возвращает название товара со страницы."""
        return self.browser.find_element(By.CSS_SELECTOR, ".product_main h1").text

    def get_product_price(self):
        """Возвращает цену товара со страницы."""
        return self.browser.find_element(By.CSS_SELECTOR, ".product_main .price_color").text

    def should_be_add_to_basket_message(self):
        assert self.is_element_present(By.CSS_SELECTOR, ".alert-success"), \
            "Сообщение о добавлении товара не найдено"

    def should_be_correct_product_name(self):
        product_name = self.get_product_name()
        message_name = self.browser.find_element(By.CSS_SELECTOR, ".alert-success strong").text
        assert product_name == message_name, \
            f"Название товара не совпадает: ожидалось '{product_name}', получено '{message_name}'"

    def should_be_basket_total_message(self):
        assert self.is_element_present(By.CSS_SELECTOR, ".alert-info"), \
            "Сообщение о стоимости корзины не найдено"

    def should_be_correct_basket_total(self):
        product_price = self.get_product_price()
        basket_total = self.browser.find_element(By.CSS_SELECTOR, ".alert-info strong").text
        assert product_price == basket_total, \
            f"Стоимость корзины не совпадает: ожидалось '{product_price}', получено '{basket_total}'"