#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "m.settings")
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(['', 'runserver'])
else:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
