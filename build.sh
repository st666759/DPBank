#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt


python manage.py collectstatic --no-input
python manage.py migrate
gunicorn myproject.wsgi:application -b 0.0.0.0:$PORT