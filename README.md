# django-rest-framework-seed

This project is a skeleton for a quickstart web API app that uses Django REST Framework. You can use it to save time and quickly bootstrap your web API projects and dev environment for these projects.

The seed contains a sample [Django REST Framework] project and a pip requirements file to easily install the [Django] and the Django REST frameworks along with the cors-headers requirement.

The seed app does the minimal which is common for most projects: enabling Token authentication and CORS headers. It comes as well with sample User and Address models, as well as their respective serializers, viewsets and urls.

## Getting Started

To get you started you can simply clone the django-rest-framework-seed repository, create a virtual env and install the dependencies:

### Prerequisites

You need **git** to clone the angular-seed repository. You can get git from http://git-scm.com/.

You need also **pip** to install the requirements of the project. It is recommended to have as well **virtualenv** to setup requirements specific to the project in a new virtual environment as well as **virtualenvwrapper** to easily switch between virtual envs. You can get them from http://docs.python-guide.org/en/latest/dev/virtualenvs/

### Clone django-rest-framework-seed

Clone the django-rest-framework-seed repository using git:
```sh
$ git clone https://github.com/o5k/django-rest-framework-seed.git
$ cd django-rest-framework-seed
```
If you just want to start a new project without the django-rest-framework-seed commit history then you can do:
```sh
$ git clone --depth=1 https://github.com/o5k/django-rest-framework-seed.git <your-project-name>
```
The depth=1 tells git to only pull down one commit worth of historical data.

### Create and activate a virtual environment

```sh
$ mkvirtualenv django-rest-framework-seed
$ workon django-rest-framework-seed
```
### Install Dependencies

Provided that you have all the prerequisites, and you have activated your virtual env, to install dependencies of the project do the following inside the project directory:
```sh
$ pip install -r requirements.txt
```

### Run the project

The simplest way to run the project is by using the built-in Django development server:
```sh
$ ./manage.py runserver
```
Now browse to the app at http://localhost:8000/

## Directory Layout

```
├── app                   -> a Django app
│   ├── admin.py          -> not used
│   ├── __init__.py       -> required to make the directory a package
│   ├── migrations        -> SQL migrations folder
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py         -> where we create our Django models
│   ├── serializers.py    -> serializers of our models
│   ├── tests.py          -> we can write our tests here
│   ├── views.py          -> we write our viewsets here
├── LICENSE
├── manage.py             -> executable to manage our project (run, makemigrations..)
├── project               -> the Django project folder
│   ├── __init__.py
│   ├── settings.py       -> all our project setting are here
│   ├── urls.py           -> we set here the URLs of our app
│   ├── wsgi.py
├── README.md
└── requirements.txt      -> the requirements of our project
```

## Contributions

Have a suggestion? Want to contribute? Great!

Please feel free to fork the repo and make a pull request or simply create an issue if you find a bug.

## License

This project is licensed under the terms of the [MIT] license.

## Contact
To get in touch about Django-REST-Framework-Seed feel free to contact me via http://oussamakrifa.com

[Django REST Framework]: http://django-rest-framework.org
[Django]: https://docs.djangoproject.com/
[MIT]: http://opensource.org/licenses/MIT