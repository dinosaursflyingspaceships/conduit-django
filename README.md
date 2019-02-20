# Conduit

## Installation

1. Install [Python 3.7.2}(https://www.python.org/downloads/release/python-372/).
2. Clone this repository: `git clone git@github.com:howardderekl/conduit-django.git`.
3. `cd` into `conduit-django`: `cd conduit-django`.
4. Install [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/#installing-virtualenv).
5. Create a new virtualenv called "ENV": `virtualenv ENV`.
6. Set the local virtualenv to "conduit": `source ENV/bin/activate`.

If all went well then your command line prompt should now start with `(ENV)`.

7. Install the required packages: `pip install -r requirements.txt`
8. project should build and run with: `python manage.py runserver`

If your command line prompt does not start with `(Env)` at this point, try running `source ENV/bin/activate` or `cd ../conduit-django`. 

If virtualenv is still not working, visit us in the Thinkster Slack channel so we can help you out.