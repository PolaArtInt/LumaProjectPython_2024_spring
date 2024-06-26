from pages.locators import SearchTermsLocators as ST
from pages.locators import BaseLocators as Base
from selene import browser, be, have, query
from selene.support.shared.jquery_style import s, ss
import allure


@allure.link('https://trello.com/c/tnpU7rqU')
def test_015_001_001_search_terms_title_is_visible():
    browser.open(ST.LINK_SEARCH_TERMS)
    s(Base.PAGE_TITLE).should(have.text("Popular Search Terms"))


@allure.link('https://trello.com/c/9oDGaMAB')
def test_015_001_002_count_search_terms():
    browser.open(ST.LINK_SEARCH_TERMS)
    ss(ST.TERMS_FOR_SEARCH_LIST_QTY).should(have.size(100))


@allure.link('https://trello.com/c/VwsOnXB6')
def test_015_001_003_check_if_search_terms_has_size_from_76_till_136():
    # assert from selenium - how to check sizes
    browser.open(ST.LINK_SEARCH_TERMS)
    list_font_sizes = []
    terms = ss(ST.LIST_OF_SEARCH_TERMS)
    for g in terms:
        g_font, g_size = g.get(query.attribute("style")).split(": ")
        g_size = float(g_size.replace("%;", ""))
        list_font_sizes.append(g_size)
    assert min(list_font_sizes) <= 76 and max(list_font_sizes) >= 136, "Font sizes not between 76 and 136"