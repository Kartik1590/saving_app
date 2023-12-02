from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'saving_app',
        'USER':'postgres',
        'PASSWORD':os.environ.get('PASSWORD'),
        'HOST':'localhost'

    }
}