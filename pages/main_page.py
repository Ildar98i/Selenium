from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Yandex_search(BasePage):
    def test_inp(self):
        inp = self.find_element((By.CSS_SELECTOR, "input.input__control"))
        inp.send_keys("Тензор")

    def test_suggest(self):
        sug = self.find_elements((By.CSS_SELECTOR, "li.mini-suggest__item"))
        assert sug != 0, "Нет таблицы с подсказками"
        suggest = self.find_element((By.CSS_SELECTOR, "li[data-text='тензор']"))
        suggest.click()

    def test_href(self):
        href = self.find_element((By.CSS_SELECTOR, "li[data-cid='0'] a")).get_attribute("href")
        assert "tensor.ru" in href, "Первая ссылка не ведет на сайт 'tensor.ru'"


class Yandex_img(BasePage):
    def test_img(self):
        img_link = 'https://yandex.ru/images/?utm_source=main_stripe_big'
        elements = self.find_elements((By.CSS_SELECTOR, "li.services-new__list-item a "))
        for element in elements:
            print(element)
            href = (element.get_attribute("href"))
            if img_link in href:
                element.click()

    def test_img_win(self):

        self.browser.switch_to.window(self.browser.window_handles[1])
        href = self.find_element((By.CSS_SELECTOR, "link[rel='alternate']")).get_attribute(
            "href")
        assert "yandex.ru/images/" in href, "Неверная ссылка"
        item = self.find_element((By.CSS_SELECTOR, "div.PopularRequestList-Item_pos_0"))
        item_name = item.get_attribute("data-grid-text")
        item.click()
        assert self.find_element((By.CSS_SELECTOR, "input.input__control")).get_attribute(
            "value") == item_name, "название категории не совпадает"

    def test_img_open(self):
        img = self.find_element((By.CSS_SELECTOR, "div.serp-item_pos_0 a img"))
        img.click()
        win_img = self.find_element((By.CSS_SELECTOR, "img.MMImage-Origin"))
        assert win_img.get_attribute("src") == img.get_attribute("src"), "картинка не открылась"

    def test_switch_img(self):
        img_first = self.find_element((By.CSS_SELECTOR, "img.MMImage-Origin")).get_attribute("src")
        button = self.find_element((By.CSS_SELECTOR, "div.CircleButton_type_next"))
        button.click()
        img_second = self.find_element((By.CSS_SELECTOR, "img.MMImage-Origin")).get_attribute("src")
        assert img_first != img_second, "Картинка не переключилась"

        button1 = self.find_element((By.CSS_SELECTOR, "div.CircleButton_type_prev"))
        button1.click()
        img = self.find_element((By.CSS_SELECTOR, "img.MMImage-Origin")).get_attribute("src")
        assert img == img_first, "Картинка не соответствует"
