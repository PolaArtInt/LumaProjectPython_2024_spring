from data.links import MEN_PAGE_URL
from selene.support.conditions import have
from selene.support.shared.jquery_style import s
from pages.components.nav_wigdet import NavComponent
from pages.locators import NavigatorLocators as Nav
from pages.locators import BaseLocators as Header
from selenium.webdriver.support.color import Color


class MenPage:

    def __init__(self, browser):
        self.browser = browser
        self.nav = NavComponent(browser)

    def open_page(self):
        self.browser.open(MEN_PAGE_URL)

    def get_current_url(self):
        return self.browser.driver.current_url

    @staticmethod
    def get_current_header():
        return s(Header.PAGE_HEADER)

    def is_loaded(self):
        self.get_current_header().should(have.text("Men"))
        is_current_page_men = self.get_current_url() == MEN_PAGE_URL
        assert is_current_page_men, "Men's page did not load successfully"

    @staticmethod
    def is_active():
        underline = Color.from_string('#ff5501').rgb
        font = Color.from_string('#333').rgba
        assert s(Nav.NAV_MEN).should(have.css_property('color', font))
        assert s(Nav.NAV_MEN).should(have.css_property('border-color', underline))
