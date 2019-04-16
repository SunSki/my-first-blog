from django.urls import path
from . import views

urlpatterns = [
    # if ~:8000/ -> wiews.post_listにルーティング
    # name='post_list' は、ビューを識別するために使われるURL の名前
    path('', views.post_list, name = 'post_list')
]