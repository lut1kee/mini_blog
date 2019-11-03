from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home),
    re_path(r'all-bloggs/$', views.all),
    re_path(r'bloggers/$', views.bloggers),
]
