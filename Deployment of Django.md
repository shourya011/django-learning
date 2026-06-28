Step 1 — Create your PythonAnywhere account

Step 2 — Open a Bash console and clone your repo
```
git clone https://github.com/shourya011/django-learning.git
```

Step 3 — Create a virtual environment and install dependencies
[[Deployment of Django]]```
cd django-learning
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Step 4 — Create the web app
-pick **"Manual configuration"**
-3.13

Step 5 — Point it at your virtualenv
/home/yourusername/django-learning/env

Step 6 — Edit the WSGI configuration file
```
import os
import sys

path = '/home/yourusername/django-learning'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'learning.settings'

os.environ['SECRET_KEY'] = 'paste-a-new-random-secret-key-here'
os.environ['DEBUG'] = 'False'
os.environ['ALLOWED_HOSTS'] = 'yourusername.pythonanywhere.com'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
command:-
```
python3 -c "import secrets; print(secrets.token_urlsafe(50))"
```
for the secret Key

Step 7 — Configure static files
- **URL:** `/static/`
- **Directory:** `/home/yourusername/django-learning/static`
  
Step 8 — Run migrations and collectstatic on the server
```
cd django-learning
python manage.py migrate
python manage.py collectstatic
```
create superuser:
```
python manage.py createsuperuser
```
Step 9 — Reload and go live
**"Reload"** button near the top — click it.
https://yourusername.pythonanywhere.com


Notes:-
1.
**How can I access the admin panel?**

Visit:

```
https://yourusername.pythonanywhere.com/admin/
```

2. The actual "ship an update" workflow
   **On your local machine**, after making a change:

```
git add .
git commit -m "describe what changed"
git push
```

**Then on PythonAnywhere**, open a Bash console:

```
cd django-learning
git pull
```

3.If you changed **models.py** (new field, new model): also run `python manage.py migrate`  
If you changed **static files** (CSS): also run `python manage.py collectstatic`
