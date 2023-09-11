#! /bin/bash

APP_PATH="app"
python $APP_PATH/manage.py makemigrations && python $APP_PATH/manage.py migrate
python $APP_PATH/manage.py runserver