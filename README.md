# Django Rest Framework w/ZingGrid

Create a REST endpoint with Django and have a working UI component enabling CRUD in minutes!

[Demo Video](https://share.getcloudapp.com/eDu9GZE4)

## System Requirements

- python (3.7.2) -> (Required) Python is required for this project
- pip (20.0.2) -> (Required) Pip is required to install python dependencies
- django -> The outlining REST framework to run our server, interact with the DB and serve up our data models to the client.
- pyenv -> (recommended) pyenv is recommended to manage your python versions and package dependencies.
- pyenv-virtualenv -> (recommended) pyenv-virtualenv is recommended to keep your python (pyenv) package dependencies from leaking out.

### Useful Links
  - Install python -> https://pip.pypa.io/en/stable/installing/
  - Install pip -> https://www.python.org/downloads/
  - Install pyenv -> https://github.com/pyenv/pyenv
  - Install pyenv-virtualenv -> https://github.com/pyenv/pyenv-virtualenv
  - Docs django -> https://www.django-rest-framework.org/tutorial/quickstart/
  - Docs django rest -> https://www.django-rest-framework.org/tutorial/1-serialization/
    - Suggested to follow steps 1-5 of the django tutorial
  
## Install Steps

I have followed this [medium guide](https://medium.com/@BennettGarner/build-your-first-rest-api-with-django-rest-framework-e394e39a482c) to get the project going, but if you already understand python and Django you can skip this.

#### Migrate Database models

It turns out that Django comes with a few models already built in. We need to migrate those built in models to our database.

```
python manage.py migrate
```

If you have added models of your own you need migrate those models with

```
python manage.py makemigrations
```

#### Create Super User

```
python manage.py createsuperuser

  Username (leave blank to use 'zingsoft'): 
  Email address: support@zingsoft.com
  Password: 
  Password (again): 
  Superuser created successfully.
```

#### Create Some Records

We need to add some records to our hero table. We can do that by starting the server and adding them.

```
python manage.py runserver
```

And then visit the admin url `localhost:8000/admin`.


#### Finally

You can visit the ZingGrid demo by starting the server and visiting the zinggrid url `localhost:8000/zinggrid`. **If the server
is already started from the previous step, skip the following command.**

```
python manage.py runserver
```

## CRUD Grid

Creating a full REST/CRUD grid is easy in ZingGrid. While the grid webcomponent itself is
highly customizable, we have some top level `<zing-grid>` tag attributes that will help
shortcut the process.

1. Start by setting the src attribute to your CRUD url

```html
<zing-grid 
    caption="Django REST Example"
    src="http://localhost:8000/heroes/">
</zing-grid>
```

or alternatively set the src using a relative path `src=/heroes/` or django's [built in](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#url) `url` to set the url dynamically if needed.

2. Add the `editor-controls` attribute to enable all CRUD functionality. We have a shortcut attribute that enables: CREATE, DELETE and UPDATE 
UI options for the grid.

```html
<!-- https://www.zinggrid.com/docs/crud/basics -->
<zing-grid 
    caption="Django REST Example"
    src="http://localhost:8000/heroes/"
    editor-controls>
</zing-grid>
```

3. Add `PUT` and `PATCH` fixes. By default ZingGrid will call `http://localhost:8000/heroes/5` and django expects a trailing slash
`ttp://localhost:8000/heroes/5/`. We can fix this two ways, in ZingGrid or on our python server.

To add a trailing slash in ZingGrid add the `urlSuffix` to append a trailing slash to requests

```html
<zing-grid 
  caption="Django REST Example"
  src="/heroes"
  editor-controls>
  <zg-data>
    <zg-param name="urlSuffix" value="/"></zg-param>
  </zg-data>
</zing-grid>
```

To add the trailing slash on your server use the `APPEND_SLASH` in your `settings.py` as directed in the [django docs](https://docs.djangoproject.com/en/dev/ref/settings/#append-slash)

4. We have an optional `django` adapter to set the `zg-params` for you

```html
<zing-grid 
    caption="Django Adapter Example"
    editor-controls>
    <zg-data adapter="django" src="/heroes"></zg-data>
</zing-grid>
```

5. You can also check out our custom Django code for the todo list demo where we modify `views.py`, `urls.py`, `models.py` and `serializers.py` to
  work with our default ZingGrid REST options.

```html
<zing-grid 
    caption="Django Custom REST Endpoint Example (Todos)"
    src="/todos"
    editor-controls>
    <zg-colgroup>
        <zg-column index="id" type="recordkey"></zg-column>
        <zg-column index="item" type="text"></zg-column>
    </zg-colgroup>
</zing-grid>
```