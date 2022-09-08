from selene import be, have
from selene.support.shared import browser

# Открытие результатов по строке поиска
def test_find(open_browser):
    browser.element('[name=q]').should(be.blank).type('selene').press_enter()

# Позитивный тест
def test_positive():
    browser.element('[id=search]').should(have.text('User-oriented Web UI browser tests in Python'))

# Негативный тест
def test_negative(after_end):
    browser.element('[id=search]').should_not(have.text('ya Chebur'))
