This sample Flask based app. [Flask](https://palletsprojects.com/p/flask/) is a very lightweight framework for developing web APIs in Python. 

When user starts the flask app, he/she gets the WARNING message and follows:

>*WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.*

As Flask does not come with a production-level server by default, as it comes with [Werkzeug](https://pypi.org/project/Werkzeug/).

-   Sample Flask App
-   Containerize using Docker
-   Configuring and running with uWsgi and nginx

Sample Flask App
=================

```
mkdir flasksample flasksample/src flasksample/static
cd flasksample
virtualenv -p python3 venv
source venv/usr/local/bin/activate
pip install -U Flask==1.1.1
pip freeze > requirements.txt
touch src/server.py src/wsgi.py src/__init__.py
```

Containerize using Docker
==========================

Description To be added later

To Run the app execute the following:
```
docker-compose up --build -d
```
To stop the app execute the following:
```
docker-compose stop
```
Configuring and running with uWsgi and nginx
==============================================
A traditional web server does not understand or have any way to run Python applications.
Python community came up with WSGI as a standard interface that modules and containers could implement. WSGI is the standard way to develop/deploy Python web applications.

Details to be added later, specially for static files which to be served using nginx.



