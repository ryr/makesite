" Settings for tests. "
from settings.project import *

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'TEST_CHARSET': 'utf8',
    }}

# Caches
CACHES['default']['KEY_PREFIX'] = '_'.join((PROJECT_NAME, 'TST'))
