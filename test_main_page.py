from pages.main_page import Yandex_search
from pages.main_page import Yandex_img


def test_yandex_search(browser):
    link = "https://yandex.ru/"
    page = Yandex_search(browser, link)
    page.open()
    page.test_inp()
    page.test_suggest()
    page.test_href()

def test_yandex_img(browser):
    link = "https://yandex.ru/"
    page = Yandex_img(browser, link)
    page.open()
    page.test_img()
    page.test_img_win()
    page.test_img_open()
    page.test_switch_img()