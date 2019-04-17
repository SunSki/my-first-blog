from django.urls import path
from . import views

urlpatterns = [
    # if '/' -> wiews.pyのpost_list にルーティング
    # name='post_list' は、ビューを識別するために使われるURL の名前
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]