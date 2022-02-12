from .common import *

DEBUG = False



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mutbly_prod',
        'USER': 'sbsstlocal',
        'PASSWORD': '1234',
        'HOST': '172.17.0.1',
        'PORT': 3306,
    }
}