# Sample project for playing with Django

## List of commands for initial setting

- `python --version`
- `pip install pipenv`
- `cd C:\dev\`
- `mkdir django`
- `ls`
- `cd .\django\`
- `mkdir storefront`
- `cd .\storefront\`
- `pipenv install django`
- `ls`
- `code .`
- `pipenv shell`

## Virtual env commands

- `cls`
- `django-admin`
- `django-admin startproject storefront`
- `django-admin startproject storefront .`
- `django-admin runserver`
- `python .\manage.py`
- `python .\manage.py runserver`
- `pipenv --venv`

## VSC shortcuts

- ```ctrl + ` ``` - opens integrated terminal window
- `ctrl + b` - open/close left panel with various options
- `ctrl + l` - clears terminal window

## Django commands

- `python manage.py startapp playground` - creates new app in the project

## Remarks

Removed depreciated app `"django.contrib.sessions"` from `settings.py`

## Django Debug Toolbar

- `pipenv install django-debug-toolbar`

## Some Extra Stuff for Windows Powershell v7

To have some mimic version of zsh like terminal that displays the git branches, follow the advice from those 2 below links:

- <https://abdullahnafees.medium.com/how-to-beef-up-your-powershell-7-with-oh-my-posh-20d6534d75eb>
- <https://ohmyposh.dev/docs/migrating>

Extra fonts:

- <https://www.nerdfonts.com/>

## Django Model field reference

- <https://docs.djangoproject.com/en/4.1/ref/models/fields/>
