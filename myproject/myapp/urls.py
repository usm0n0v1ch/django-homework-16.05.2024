from django.urls import path

from myapp import views


urlpatterns = [
    path('', views.article_list, name='index.html'),
]