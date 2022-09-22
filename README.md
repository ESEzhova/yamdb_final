![workflow](https://github.com/ESEzhova/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# yamdb

# Проект, который собирает отзывы пользователей на произведения.

## Описание

### Произведения делятся на категории: «Книги», «Фильмы», «Музыка» (возможно расширение списка админом).

### Сами произведения в проекте не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

### В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха.

### Произведению может быть присвоен жанр «Сказка», «Рок» или «Артхаус» (возможно расширение списка админом).

### Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти; из пользовательских оценок формируется усреднённая оценка произведения — рейтинг. На одно произведение пользователь может оставить только один отзыв.

### Реализована аутентификация по токену.

## Запуск проекта на сервере:

### 1. Сделать fork проекта в свой GitHUB;



### 2. В разделе проекта Setting/Secrets указать логин и пароль DockerHUB с ключами:

```
DOCKER_USERNAME, DOCKER_PASSWORD
```


### 3. В разделе проекта Setting/Secrets указать параметры (хост, логин, ssh-key, пароль ) DockerHUB с ключами:

```
HOST, USER, SSH_KEY, PASSPHRASE
```


### 4. В разделе проекта Setting/Secrets указать параметры базы данных с ключами:

```
DB_ENGINE, DB_NAME , POSTGRES_USER, POSTGRES_PASSWORD, DB_HOST, DB_PORT
```


### 5. В разделе проекта Setting/Secrets указать параметры базы данных с ключами:

```
DB_ENGINE, DB_NAME , POSTGRES_USER, POSTGRES_PASSWORD, DB_HOST, DB_PORT
```

### 6. В разделе проекта Setting/Secrets указать ID телеграм-канала и токен телеграм-бота для получения уведомлений с ключами:

```
TELEGRAM_TO, TELEGRAM_TOKEN
```

### 7. Подготовить сервер:

#### - Остановить службу nginx:
```
 sudo systemctl stop nginx 
```
#### - Установить докер:
```
 sudo apt install docker.io 
```

#### - Установить docker-compose в соответствии с официальной документацией;


#### - Скопировать файлы docker-compose.yaml и nginx/default.conf из проекта на сервер в home/<ваш_username>/docker-compose.yaml и home/<ваш_username>/nginx/default.conf соответственно.


### 8. На GitHUB выполнить commit, после которого запустятся процедуры workflow;



### 9. На сервере выполнить миграции, создать суперюзера, собрать статику:

```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input

```


### 10. Набрать в браузере:

```
http://<ip_сервера>/admin
```

### Работоспособность приложения можно проверить без развертывания на уже запущенном сервере:

```
http://84.252.142.36/admin
```


## Примеры

### Когда вы запустите проект, по адресу http://<ip_сервера>/redoc/ будет доступна документация для API YaMDb. В документации описаны примеры работы API. Документация представлена в формате Redoc.

## Стек технологий

### Python 3, Django 2.2, Django REST framework, SQLite3, Simple-JWT, PostgreSQL, Nginx, Docker