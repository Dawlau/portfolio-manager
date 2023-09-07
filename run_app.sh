#! /bin/bash

APP_PATH="config"
python $APP_PATH/manage.py makemigrations && python $APP_PATH/manage.py migrate
python $APP_PATH/manage.py runserver