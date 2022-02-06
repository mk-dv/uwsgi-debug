# Django & UWSGI

A small application for testing the integration of the Pycharm debugger with uwsgi 


Run -> Edit Configurations -> Add new configuration -> Python Debug Server
and run it
Then - run uwsgi server:
    uwsgi --http :8000 --module uwsgi_debug.wsgi
