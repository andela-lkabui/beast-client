from django.conf.urls import url

from oxford_api import views

urlpatterns = [
  url(r'search', views.search, name='search')  
]