from .common import *

SECRET_KEY = '8+ize@+ae1(d32+(pk_p7!&%@d#o_&*i$5ojpr-1zd_1aer)(o'

DEBUG = True

ALLOWED_HOSTS = ['*']

# 搜索设置
HAYSTACK_CONNECTIONS['default']['URL'] = 'http://elasticsearch_local:9200/'
