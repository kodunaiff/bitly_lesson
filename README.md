# Обрезка ссылок с помощью Битли
________________
Скрипт сокращает длинную ссылку или выводит количество переходов по ней, 
если она короткая. Мы будем использовать Сервис Bitly. 

## Как установить
Скачайте или клонируйте проект, создайте файл ".env" с таким содержимым:
````
TOKEN = Здесь ваш GENERIC ACCESS TOKEN
````
## Как получить GENERIC ACCESS TOKEN

* Вам необходимо перейти на сайт https://bitly.com
* Создайте себе аккаунт https://bitly.com/a/sign_up.
* Если у вас есть аккаунт, то авторизуйтесь https://bitly.com/a/sign_in.
* Перейдите на страницу настроек https://bitly.com/a/settings
* Выберите вкладку «Generic Access Token»
* Введите ваш пароль от bit.ly и кликните «Generate Token»
* Скопируйте ваш «Generic Access Token» и вставьте его в файл .env

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
````
pip install -r requirements.txt
````

### Пример запуска

````
python main.py https://www.google.com/
````

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.