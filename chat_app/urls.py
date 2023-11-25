from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('<str:room>/', views.room, name='room'),  # it is dynamic and collects all rooms
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]