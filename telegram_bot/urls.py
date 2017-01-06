from django.conf.urls import url

from telegram_bot import views

urlpatterns = [
  url(r'webhook', views.webhook_handler, name='webhook')  
]