from .common import *

SECRET_KEY = '8+ize@+ae1(d32+(pk_p7!&%@d#o_&*i$5ojpr-1zd_1aer)(o'

DEBUG = False

ALLOWED_HOSTS = ['www.themortal.xyz']
HAYSTACK_CONNECTIONS['default']['URL'] = 'http://TheMortal_elasticsearch:9200/'
