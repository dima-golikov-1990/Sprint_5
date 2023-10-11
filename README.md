# Автотесты для сервиса Stellar Burgers

Автотесты покрывают функционал:
- Регистрация
- Авторизация
- Навигация по сервису
- Выход из системы

Проект включает файлы:
- conftest.py - файл конфигурации для автотестов
- login.py - автотесты по авторизации
- logout.py - автотесты по выходу из системы
- navigation.py - автотесты по навигации
- registration.py - автотесты по регистрации

Список автотестов:
- Регистрация:
  - test_reginstration_with_valid_password - регистрация с валидным паролем
  - test_reginstration_with_invalid_password - регистрация с невалидным паролем


- Авторизация:
    - test_login_using_the_login_to_account_button - авторизация через кнопку "Войти в аккаунт"
    - test_login_using_the_account_button - авторизация через кнопку "Личный кабинет"
    - test_login_in_registration_page - авторизация через кнопку в форме регистрации
    - test_login_in_recover_password_page - через кнопку в форме восстановления пароля


- Навигация:
  - test_navigation_to_account - переход по клику на "Личный кабинет"
  - test_navigation_from_account_to_constructor - переход из личного кабинета в конструктор
  - test_navigation_from_account_to_constructor_use_click_logo - переход из личного кабинета в конструктор через нажатие на лого Stellar Burgers
  - test_navigation_tab_buns - переход в раздел "Булки"
  - test_navigation_tab_sauces - переход в раздел "Соусы"
  - test_navigation_tab_fillings - переход в раздел "Начинки"

- Выход из системы:
  - test_logout_from_profile - выход из системы
































































