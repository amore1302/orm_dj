﻿# Локальный сай - пульт охраны банка

Сайт помогает отслеживать кто был в хранилище банка в Вашем филиале.
Это внутренний репозитарий для сотрудников банка.

### Как инсталировать



На компьютере должен быть установлен Python3
Таже  должен быть установлен   `pip` or `pip3`  :
Для инсталяции приложения используйте команду
```
pip install -r requirements.txt
```

### Сайт запусется командой
```
python manage.py runserver 0.0.0.0:8000
```
Сайт запускается один раз.
после того как сайт запущен посмотреть кто пользуется хранилищем
можно через любой браузер выполнив в нем переход по адресу : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Настройка среды файл .env
Перед запуском программы нужно настроить в .env файле параметры среды окружения.
Без настройки параметров сайт работать не будет.
Вот эти параметры
1. ENGINE=
1. HOST=
1. PORT=
1. NAME=
1. USER=
1. PASSWORD=
1. SECRET_KEY=

### Цель проекта

Этот код написан в учебный целях. Цель научиться разворачивать сайт(написан на джанго)
на локальном компьютере.
Этот учебный проект написан по уроку с сайта  [dvmn.org](https://dvmn.org/).