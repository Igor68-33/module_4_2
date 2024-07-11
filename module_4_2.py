# Пространство имен
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    name_of_test_function = [func for func in locals()]  # список доступных имён
    print('Список имён test_function: ', name_of_test_function)
    inner_function()


name_of_main = [func for func in locals()]  # список доступных имён
print('Список имён глобальных: ', name_of_main)
test_function()
# inner_function() # Ошибка при написании: Unresolved reference 'inner_function'
# при выполнении inner_function() получим предупреждение о недопустимости вызова этой функции
# в области видимости глобальных имён:
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
