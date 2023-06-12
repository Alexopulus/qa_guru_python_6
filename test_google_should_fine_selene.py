from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture(scope='session')
def window_size():
    browser.config.window_width = 1024
    browser.config.window_height = 768


def test_should_find_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="center_col"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_shouldnt_find_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('awdawd123123123212').press_enter()
    browser.element('[id="center_col"]').should(have.text('не найдено'))
