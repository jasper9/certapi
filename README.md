# certapi

## What is this
This is the skeleton of an application that could be grown to be an [ACME](https://en.wikipedia.org/wiki/Automated_Certificate_Management_Environment) compliant certificate authority.  It is made with Python3 + Flask + Gunicorn.

## How to Run
This could be run a multiple of different ways (locally, in a container, virtualenv, pipenv... ).  Documenting how to run via a docker container here.

### Run locally via prebuilt container
Run this application in a local container with the following:
```bash
git clone https://github.com/jasper9/certapi.git
cp ./certapi/config.ini.example ./certapi/config.ini
docker run --rm -v `pwd`/certapi:/code -p 80:8080 jasper9/certapi
```
## Configuration
To modify the sleep time edit `config.ini`
```bash
[system]
domain = localhost
sleep_time = 10
```

## Tasks
- [x] properly handles certificates for different domain
  * Domain is a url string parameter.

- [x] Allows certificates to live for 10 minutes before expiring
  * Stubbed.  The task was to stub the generation of the certs 
themselves.  If I was to implement this, the expiry is a field in the 
cert.  In the past i've used the crypto python library like the following:

cert = crypto.X509()
...
cert.gmtime_adj_notAfter(10*365*24)
...
etc

- [x] Sleeps for 10 seconds when a new certificate is generated
  * Done.  Sleep is in the common functions file.  Although this requirement 
makes very little sense to me as you normally want api responses to be fast 
and fork a thread to any long running async work.   ¯\\_(ツ)_/¯

- [x] Generates its own certificate and keeps its certificate up-to-date when it expires 
it expires
  * Done.  This is solved by using the @app.before_request decorator in 
main.py.   If this was production I probably would have implemented flask's 
scheduler to invoke this check once a day instead of on every request for 
better performance

- [x] can generate multiple certificates at the same time
  * Done.  Solved by making flask run in multiple threads so that one of
the 10s sleeps doesn't impact another.

## Backlog
- API documentation
  * Use the flask restplus library which creates the swagger definitions.
- Create certificates
- Parameterize certificate fields and options
- Implement actual ACME specification
- Remove debug flag from flask startup