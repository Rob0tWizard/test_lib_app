import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service.library.settings')

app = Celery('service')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url=settings.CELERY_BROKER_URL
app.autodiscover_tasks()
