#!/usr/bin/env bash

set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate

python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); u, _ = User.objects.get_or_create(username='user'); u.is_staff=True; u.is_superuser=True; u.set_password('user'); u.save(); print('Demo admin user is ready')"