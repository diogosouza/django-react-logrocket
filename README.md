# React App + Django API

A simple integration between Django API and React App

This project is made up of two main ones:

- *students*: the Django project containing the REST API, along with all the back-end code;
- *students-fe*: the React project, with all Node dependencies, configs, and front-end related stuff.

## Run it locally

In order to run the projects locally, you need to have Node, npm and Python installed on your machine.

### Running the Django project

Make sure you have python3 installed in your machine.

First, let's create the python virtual environment to isolate our projects:

```bash
python3 -m venv logrocket_env
```

Then, activate it:

```bash
source logrocket_env/bin/activate
```

Just then you can clone the project from GitHub. So, `cd` into the venv and run:

```bash
git clone https://github.com/diogosouza/django-react-logrocket.git
```

Now, add the needed Djano dependencies:

```bash
pip install django djangorestframework django-cors-headers
```

Great, just need to run the project now. For this, `cd` into the django-react-logrocket folder and run:

```bash
python manage.py runserver
```

That's it. Access the address http://localhost:8000/api/students/ and check for the API up and running.

### Running the React project

First, `cd` the students-fe directory and run:

```bash
npm install
```

Then, you just need to run the app via:

```bash
npm start
```

