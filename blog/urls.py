from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('upload/', views.upload_post, name='upload_post'),
]
