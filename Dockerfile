FROM python:3.9.0

WORKDIR /home/

RUN echo "dueno"

RUN git clone https://github.com/hanbitgoun/djangoproject_02.git

WORKDIR /home/djangoproject_02/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=djangoProject.settings.deploy && python manage.py migrate --settings=djangoProject.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=djangoProject.settings.deploy djangoProject.wsgi --bind 0.0.0.0:8000"]