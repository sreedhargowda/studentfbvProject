from django.contrib import admin
from django.urls import re_path
from myApp import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.display, name='display'),
    re_path(r'^insert/', views.insert_view, name='insert'),
    re_path(r'^update/(?P<id>\d+)/', views.update_view, name='update'),
    re_path(r'^delete/(?P<id>\d+)/', views.delete_view, name='delete')
]
