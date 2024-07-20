<h1 align="center">Ultimate Django Template</h1>
<h3 align="center">A compleat foundation for starting a django project</h3>
<p align="center">
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a>
<a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a>
<a href="https://www.django-rest-framework.org/" target="_blank"> <img src="https://www.django-rest-framework.org/img/logo.png" alt="restframework" width="90" height="40"/> </a>
<a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a>
<a href="https://jwt.io/" target="_blank"> <img src="https://jwt.io/img/icon.svg" alt="jwt" width="40" height="40"/> </a>
<a href="https://swagger.io/" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/354420/swagger.svg" alt="swagger" width="40" height="40"/> </a>
<a href="https://swagger.io/" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/354272/redis.svg" alt="redis" width="40" height="40"/> </a>
<!-- <a href="https://www.gunicorn.org" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/gunicorn/gunicorn-icon.svg" alt="gunicorn" width="40" height="40"/> </a>
<a href="https://www.nginx.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/nginx/nginx-icon.svg" alt="nginx" width="40" height="40"/> </a> -->

</p>

[![Code Style Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

<h1 align="center">Aspects</h1>

### General features
- Dockerized
- Django RestFramewok
- Authentication
- SMTP4DEV
- Django Debug Toolbar

### Authentication method
- Jason Web Token ( JWT )
- Token
- Basic
- Session

### Database
- PostgreSQL

### Reformatting method
- Flake8
- Black

### Changing method
- Redis
- Celery

### Documentation
- Swagger
- Reduc

<h1 align="center">Setup</h1>

### Clone
To get the repository you need to run this command in git terminal
```bash
git clone https://github.com/Benfoxyy/Ultimate-Django-Template-4.2.git
```

### Getting ready

The project is base on docker so lets start <a href='https://docs.docker.com/engine/install/'>docker</a> and using the app
```bash
docker-compose up -d --build
```

Once you have installed django and other packages, go to the cloned repo directory and ru fallowing command
```bash
docker-compose exec sh -c "python manage.py makemigrations"
```

This command will create all migrations file to database

Now, to apply this migrations run following command
```bash
docker-compose exec sh -c "python manage.py migrate"
```

Now you can go to a browser and type http://127.0.0.1:8000 and see the resault!

<hr>

### Access to admin panel
For editing or manage the database, you shulde be superuser and have superuser permission. So lets create superuser
```bash
docker-compose exec sh -c "python manage.py createsuperuser"
```
- Email
- Password
- Password confirmation

Thene you can now go in admin panel with http://127.0.0.1:8000/admin/

<hr>

<h3 align='center'>Thanks for visiting my app, if you have any opinions or seeing bugs; let me know 🙂</h3>