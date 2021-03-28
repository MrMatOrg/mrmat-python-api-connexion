# MrMat :: Python :: Flask API :: Spec-First

Boilerplate code for a Python Flask API using Connexion

[![Build](https://github.com/MrMatOrg/mrmat-python-api-connexion/actions/workflows/build.yml/badge.svg)](https://github.com/MrMatOrg/mrmat-python-api-connexion/actions/workflows/build.yml)
[![SAST](https://github.com/MrMatOrg/mrmat-python-api-connexion/actions/workflows/sast.yml/badge.svg)](https://github.com/MrMatOrg/mrmat-python-api-connexion/actions/workflows/sast.yml)


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

You have the choice of running this directly or within a container image. To run this directly (assuming you have create
the recommended virtualenv):

```
$ pip install -r requirements.txt
$ python ./setup.py install
$ mrmat-python-api-connexion -h
usage: mrmat-python-api-connexion [-h] [-d] [--host HOST] [--port PORT]

mrmat-python-api-connexion - 0.0.2

optional arguments:
  -h, --help   show this help message and exit
  -d, --debug  Debug
  --host HOST  Host interface to bind to
  --port PORT  Port to bind to

$ mrmat-python-api-flask --host 0.0.0.0 --port 8080
 * Serving Flask app "mrmat_python_api_connexion.app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)

 
<Ctrl-C>
```

To run within a container, first build that container:

```
$ python ./setup.py sdist
$ docker build -t mrmat-python-api-connexion:0.0.2 -f var/docker/Dockerfile .
...
$ docker run --rm mrmat-python-api-connexion:0.0.2
...
```

## How to use this

Once started, you can curl towards the APIs mounted as defined by their base_path declared at the top of `mrmat_python_api_connexion/app.py`.
The Swagger UI is available by appending `/ui` to that base path.

>Note that omitting the last slash will cause a redirect that you can follow using curls -L option. We can probably
>get rid of that by using a more clever versioning scheme that doesn't make the root resource listen on / (e.g. `/greeting`).

## How to test this

Unit tests are within the `tests` directory. You can use the built-in Pycharm test configuration or do it on the CLI.

```
$ python ./setup.py install
$ python -m flake8
$ python -m pytest
```
