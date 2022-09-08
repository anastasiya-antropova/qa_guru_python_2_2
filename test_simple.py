#фикстура в pytest - функция, которая умеет выполнять опр код до теста и после теста (для очистки мусора
#бывают явные и неявные
#неявные - через scope (момент вызова)
#фикстуры могут возвращать значение - return

import pytest

@pytest.fixture(scope="session", autouse=True) #вызывается в любом случае, типа глобальная
def open_browser():
    print("Я - фикстура, выполняюсь перед тестом!") #setup то, что выполняется перед тестом
    yield #тут выполняется тест, обязательно перед тирдауном
    print("Я выполняюсь после теста") #тирдаун постусловие

@pytest.fixture()
def choice_user():
    #выбор клиента
    user_id=123
    #return user_id #альтернативный синтаксис для предтеста
    yield user_id #возвращает значение и передает управление дальше
    print("Удаляем пользователя 123")

@pytest.fixture()
#def configure_mobile_browser(open_browser):  - когда указывали явно, без указания неявно
def configure_mobile_browser():
    #объявление документации
    """Устанавливаем мобильное соотношение сторон браузера"""
    print("Я - мобильный!")

@pytest.fixture()
#def configure_desctop_browser(open_browser): - когда указывали явно, без указания неявно
def configure_desctop_browser():
    """Устанавливаем десктопное соотношение сторон браузера"""
    print("Я - десктопный!")

# Авторизуемся на гитхаб
# Создаем репозиторий
# Открываем readme.md
#def test_first(open_browser, configure_mobile_browser): - когда указывали явно, без указания неявно
def test_first(configure_mobile_browser):
    print(configure_mobile_browser)
    #pass # используем, если б не было принта или пр, просто слово, ниче не делает, надо чтобы не пустое тело было

#def test_second(configure_desctop_browser, open_browser): - когда указывали явно, без указания неявно
def test_second(configure_desctop_browser):
    print(configure_desctop_browser)
    assert 1==1

def test_third(choice_user):
    print(choice_user)
    assert choice_user==123
