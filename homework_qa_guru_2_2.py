from selene import be, have
from selene.support.shared import browser

# Открытие результатов по строке поиска
def test_find(size_window, open_browser):
    browser.element('[name=q]').should(be.blank).type('selene').press_enter()

# Поиск нужного результата среди всего пула
def test_open_page():
    browser.element('[id=search]').should(have.text('User-oriented Web UI browser tests in Python'))

# Провальный тест
def test_open_yandex(after_end):
    browser.element('[button=yandex]').press_enter()