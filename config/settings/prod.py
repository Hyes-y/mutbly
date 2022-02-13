from .common import *

'''
def read_secret(secret_name):
    file = open("/run/secrets/" + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()

    return secret


SECRET_KEY = read_secret("DJANGO_SECRET_KEY")
'''


DEBUG = False

STATICFILES_DIRS = []

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