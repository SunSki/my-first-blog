from django.urls import path
from . import views

urlpatterns = [
    # if '/' -> wiews.pyのpost_list にルーティング
    # name='post_list' は、ビューを識別するために使われるURL の名前
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('txtGen/', views.txtGen, name='txtGen'),
    path('txtGen/raw/', views.txtGen_raw, name='txtGen_raw')
]