from final import views
from django.urls import path, include

app_name = 'final'

urlpatterns = [
    path(r'^index/', views.index, name='my_index'),
    path(r'^movies/', views.movie, name='my_movies'),
    path(r'^hello/', views.hello, name='hello'),
    path(r'^blog', views.blog, name='my_blog'),
    path('phones/', views.phone, name='my_phones'),
    path('houses/', views.house, name='my_houses'),
    path('articles/', views.article, name='my_articles'),
]