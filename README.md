# StepikSeleniumFinalProject
Creation of the first full-fledged test project!

base_page.py - хранение методов, которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать.

locators.py - хранение локаторов, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать

main_page.py - хранение методов по конкретной странице, завернутые в класс этой странице. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py

test_main_page.py - выполнение самих тестов. Вызванные функции будут запускаться здесь.

Здесь мы будем создавать функции, которым:
-Выдаём нужный для проверки линк
-Создаём в функции переменную page, которой передаём браузер из base_page.py(класс BasePage) и линк из первого шага
-Следом говорим "page, откройся", но методом из base_page.py(класс BasePage)
-Добавляем проверки, которые создавали методами в main_page.py
