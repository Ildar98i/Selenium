from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator))
