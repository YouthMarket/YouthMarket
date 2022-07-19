from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:room_info>/', views.room, name='room'),
    # path('<int:post_id>/', views.chat, name='chat'),
]