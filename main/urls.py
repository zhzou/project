from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='index'),
    path('verify_page', views.verify, name='verify'),
    path('search_main', views.search_main, name='search_main'),
    path('additem_main', views.additem_main, name='additem_main'),
    path('item_main', views.item_main, name='item_main'),
    path('follow_main', views.follow_main, name='follow_main'),
    path('user_main', views.user_main, name='user_main'),
    path('follower_main', views.follower_main, name='follower_main'),
    path('following_main', views.following_main, name='following_main'),
    path('like_main', views.like_main, name='like_main'),
    path('unlike_main', views.unlike_main, name='unlike_main'),
    path('upload', views.upload, name='upload'),
    path('getmedia', views.getmedia, name='getmedia'),
    
]