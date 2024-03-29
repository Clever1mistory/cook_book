# Поварская книга на Django

Данное приложение представляет собой небольшую поварскую книгу, разработанную на Django. В приложении реализован функционал управления продуктами и рецептами, а также некоторые полезные операции.

## Установка

1. Клонируйте репозиторий на ваш локальный компьютер:
```
   git clone https://github.com/Clever1mistory/cook_book
```
2. Перейдите в папку с проектом:
```
   cd test_case
```
3. Установите зависимости, указанные в файле requirements.txt:
```
   pip install -r requirements.txt
```
4. Выполните миграции для создания необходимых таблиц в базе данных:
```
   python manage.py migrate
```
5. Запустите сервер разработки Django:
```
   python manage.py runserver
```
6. Приложение будет доступно по адресу http://localhost:8000/.

## Функционал

Приложение предоставляет следующие функции:

1. Добавление продукта в рецепт:
   - URL: /add_product_to_recipe
   - Метод: GET
   - Параметры:
     - recipe_id - идентификатор рецепта, к которому добавляется продукт
     - product_id - идентификатор продукта, который добавляется в рецепт
     - weight - вес продукта в граммах
   - Описание: Добавляет указанный продукт в указанный рецепт с указанным весом. Если продукт уже присутствует в рецепте, то обновляет его вес.
   - Пример запроса: /add_product_to_recipe?recipe_id=1&product_id=1&weight=200

2. Приготовление рецепта:
   - URL: /cook_recipe
   - Метод: GET
   - Параметры:
     - recipe_id - идентификатор рецепта, который будет приготовлен
   - Описание: Увеличивает количество приготовленных блюд для каждого продукта, входящего в указанный рецепт, на единицу.
   - Пример запроса: /cook_recipe?recipe_id=1

3. Отображение рецептов без указанного продукта:
   - URL: /show_recipes_without_product
   - Метод: GET
   - Параметры:
     - product_id - идентификатор продукта, наличие которого проверяется в рецептах
   - Описание: Возвращает список рецептов, в которых указанный продукт отсутствует или его вес меньше 10 грамм.
   - Пример запроса: /show_recipes_without_product?product_id=1

## Админка

Приложение также содержит админку, где можно управлять продуктами и рецептами. Для доступа к админке выполните следующие действия:

1. Создайте суперпользователя с помощью команды:
```
   python manage.py createsuperuser
```
2. Запустите сервер разработки Django:
```
   python manage.py runserver
```
3. Перейдите в админку по адресу http://localhost:8000/admin и войдите, используя созданные учетные данные.

В админке вы можете добавлять, редактировать и удалять продукты и рецепты, а также управлять связями между ними.

## Автор
Clever1mistory
