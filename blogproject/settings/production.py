from .common import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['www.themortal.xyz']
HAYSTACK_CONNECTIONS['default']['URL'] = 'http://TheMortal_elasticsearch:9200/'
