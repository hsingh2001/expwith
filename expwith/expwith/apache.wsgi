import os
import sys

path = '/home/ubuntu/code/expwith'
if path not in sys.path:
    sys.path.append(path)

path = '/home/ubuntu/code/expwith/expwith'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'expwith.settings'
#os.environ.setdefault('DJANGO_SETTINGS_MODULE') = 'expwith.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

