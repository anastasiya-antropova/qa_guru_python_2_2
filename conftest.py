#файл с общими штуками типа фикстур и хуки (шо такое - будет потом занятие)
#то, что лежит здесь - используется для всего проекта
#ща закомменчено чтобы не мешало
#@pytest.fixture(scope="session", autouse=True) #вызывается в любом случае, типа глобальная
#def open_browser():
#    print("Я - фикстура, выполняюсь перед тестом!") #setup то, что выполняется перед тестом
#    yield #тут выполняется тест, обязательно перед тирдауном
#    print("Я выполняюсь после теста") #тирдаун постусловие


import pytest
from selene.support.shared import browser

# Выставление размера браузера
@pytest.fixture(autouse=True)
def size_window():
    browser.config.window_height = 1900
    browser.config.window_width = 1200

# Открытие браузера
@pytest.fixture()
def open_browser():
    browser.open('https://google.com')
    print("Браузер открыт")
    yield
    print("Тест проведен")