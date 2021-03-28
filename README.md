# MrMat :: Python :: Flask API :: Spec-First

Boilerplate code for a Python Flask API using Connexion

[![Build](https://github.com/MrMatOrg/mrmat-python-flask-api/actions/workflows/build.yml/badge.svg)](https://github.com/MrMatOrg/mrmat-python-flask-api/actions/workflows/build.yml)
[![SAST](https://github.com/MrMatOrg/mrmat-python-flask-api/actions/workflows/sast.yml/badge.svg)](https://github.com/MrMatOrg/mrmat-python-flask-api/actions/workflows/sast.yml)


This variant of a Python Flask API is spec-first and using [Connexion](https://github.com/zalando/connexion) to 
implement that capability. Also see [Connexion Documentation](https://connexion.readthedocs.io/en/latest/)

Features:

* Spec-first
* Multiple API versions
* Configurability via command line
* No TLS, because this is intended to run behind a reverse proxy
* Healthz
* No OAuth 2, there are still some [issues](https://github.com/zalando/connexion/issues/549) with Connexion to support that

## How to run this

Start with `mrmat-python-flask-api`. You can specify `--host 0.0.0.0` to listen on a specific API and `--port PORT` to
override the default 8080.

Once started, you can do curl towards the greeting API at `/api/greeting/0.1/` and `/api/greeting/0.1/?name=Custom`. 
Note that omitting the last slash will cause a redirect that you can follow using curls -L option. We can probably
get rid of that by using a more clever versioning scheme that doesn't make the root resource listen on / (e.g. `/greeting`).

You can also navigate to `/api/greeting/0.1/ui` to get to the Swagger UI.

## How to test this

Pycharm built-in. If you do it on the CLI, you do need `python -m pytest`, otherwise it'll get confused about loading
its modules. Also note that the API spec yaml must be added once more when testing in `conftest.py`. The obvious attempt
to have that done straight within `mrmat_python_flask_api/app.py` outside main doesn't work (and I don't know why).

## How to build this

See the provided Dockerfile in `var/docker`. This requires that you have run `python ./setup.py sdist` as a prerequisite
and will create a container image in which the application is run within a production-ready WSGI server.
