import pytest
from selene import browser, be, have, by


@pytest.fixture(scope="function",autouse=True)
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


def test_search_google():
    browser.open('https://google.com')
    if browser.element(by.text('Принять все')).matching(be.visible):
        browser.element(by.text('Принять все')).click()
    browser.element('[name = "q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id = "search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_another_search(browser_size):
    browser.open('https://google.com')
    if browser.element(by.text('Принять все')).matching(be.visible):
        browser.element(by.text('Принять все')).click()
    browser.element('[name = "q"]').should(be.blank).type('**??:%%%').press_enter()
    browser.element('[id = "search"]').should(have.text('Похоже, по вашему запросу нет полезных результатов'))
