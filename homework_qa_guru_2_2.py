from selene import be, have
from selene.support.shared import browser

# Позитивный тест
def test_positive(open_browser):
    browser.element('[name=q]').should(be.blank).type('selene').press_enter()
    browser.element('[id=search]').should(have.text('User-oriented Web UI browser tests in Python'))

# Негативный тест
def test_negative(open_browser):
    browser.element('[name=q]').should(be.blank).type('selene').press_enter()
    browser.element('[id=search]').should_not(have.text('ya Chebur'))
