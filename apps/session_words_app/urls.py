from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),
    url(r'session_words_app/input',views.input),     
    url(r'session_words_app/clear',views.clear),
  ]