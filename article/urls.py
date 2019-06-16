from django.urls import path, include
from . import views

app_name = 'article'

urlpatterns = [
    path('article-list/', views.article_list, name='article_list'),
    path('hello/', views.blog, name='blog'),
    path('blog/<int:id>/', views.article_detail, name='blog'),
    path('blog-write/', views.article_create, name='blog-write'),
    path('blog-delete/<int:id>/', views.article_delete, name='blog-delete'),
]