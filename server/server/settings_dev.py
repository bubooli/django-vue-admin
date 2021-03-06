from .settings import *

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# celery配置
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

MYSQL_HOST = '192.168.31.134'
MYSQL_PORT = '3306'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'HOST': MYSQL_HOST,  # 数据库主机
#         'PORT': MYSQL_PORT,  # 数据库端口
#         'USER': 'root',  # 数据库用户名
#         'PASSWORD': 'admin123',  # 数据库用户密码
#         'NAME': 'vue_admin'  # 数据库名字
#     }
# }
