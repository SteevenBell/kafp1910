## Установка

Действия выполнены в ОС **Debian 11 Bullseye**.

#### - Обновим список доступных пакетов ПО из официальных репозиториев командой

```bash
sudo apt update
```

#### - Установить пакетный менеджер для Python

```bash
sudo apt install python3-pip
```

#### - Создаем папку "site" и клонируем туда проект

```bash
git clone https://github.com/SteevenBell/kafp1910.git
```

#### - Установим Postgres

```bash
sudo apt install postgresql postgresql-contrib
```
> Проверить запущена ли служба:
```bash
sudo systemctl status postgresql
```

> Если нет, то запустить:
```bash
sudo systemctl start postgresql
```

##### Создаем новую БД "kafp" с помощью стандартного пользователя postgres:
```bash
sudo su - postgres
psql
```
```sql
create database kafp;
```


##### Создаем нового пользователя БД "admin_db" и даем все привилегии:
```sql
create user admin_db with password 'admin';
GRANT ALL PRIVILEGES ON DATABASE kafp TO admin_db;
```

#### - В папке проект выполним установку всех необходимых библиотек для работы проекта:

```bash
pip3 install -r requirements.txt
```

#### - Установим gunicorn

```bash
sudo apt install gunicorn3
```

#### - Далее, нужно добавить файл .env в папку проекта, который устанавливает переменные среды для работы веб-приложения. В этом файле пропишем:
> CONFIG_MODE = prod

> PRODUCTION_DATABASE_URL = "postgresql+psycopg2://admin_db:admin@127.0.0.1:5432/kafp"

#### - В home директории изменим файл .bashrc. В начало файла следует записать:

> PATH="/home/osboxes/.local/bin:${PATH}"
export PATH

Это редактирует переменную окружения PATH, для того чтобы иметь доступ к установленным библиотекам.

#### - Выполним миграции. Перейдем в папку проекта и выполним следующие команды:

```bash
export FLASK_APP=kapf_app.py
flask db upgrade
```

#### - Установим nginx и добавим в автозапуск:

```bash
sudo apt install nginx
sudo systemctl enable nginx
```

#### - Удалим дэфолтный сайт nginx:

```bash
cd /etc/nginx/sites-available/
sudo rm default
```

###### Здесь же создаем новый файл "default" с содержимым:
```
  server {
    listen 80;
    server_name kafp.com;
    access_log  /var/log/nginx/kafp.log;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
  }

```

#### - Перезагружаем nginx:

```bash
sudo service nginx restart
```

------------

###### Открываем страницу браузера по адресу http://127.0.0.1:80. Убеждаемся, что приложение работает. Nginx "слушает" порт 80 и "пробрасывает" соединение на порт 8000 на котором запущен gunicorn.
