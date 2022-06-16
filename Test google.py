import pytest
from selene import have
from selene.browser import element
from selene.support.shared import browser


@pytest.fixture(scope='session')
def browser():
    browser.open(https // www.google.ru )
    browser.set_window_size(1920, 1080)

def positive_test(browser):
    browser.element('[title="Поиск"]')
    type('selene')
    press_enter()
    browser.element('[id=search]')
    should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))




def nagative_test(browser):
    browser.element('[title="Поиск"]')
    type('seleneiim')
    press_enter()
    browser.element('[id=search]')
    should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))












