"""
WSGI config for axdf project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# from settings import ENVIRONMENT

if sys.platform <> "win32":
    os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-eggs'

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "axdf.settings")

application = get_wsgi_application()
