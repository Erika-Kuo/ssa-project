from django.urls import path
from . import views

urlpatterns = [
   path("", views.home, name="home"),
   path('create_group/', views.create_group, name='create_group'),
   path('group//', views.group_detail, name='group_detail'),
   path('group//invite/', views.invite_users, name='invite_users'),
   path('group//delete/', views.delete_group, name='delete_group'),
]