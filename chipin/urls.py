from django.urls import path
from . import views
urlpatterns = [
   path("", views.home, name="home"),
   path('create_group/', views.create_group, name='create_group'),
   path('group/<int:group_id>/', views.group_detail, name='group_detail'),
   path('group/<int:group_id>/invite/', views.invite_users, name='invite_users'),
   path('group/<int:group_id>/accept/', views.accept_invite, name='accept_invite'),
   path('group/<int:group_id>/delete/', views.delete_group, name='delete_group'),
   path('delete-join-request/<int:request_id>/', views.delete_join_request, name='delete_join_request'),
   path('group/<int:group_id>/request-to-join/', views.request_to_join_group, name='request_to_join_group'),
   path('group/<int:group_id>/leave/', views.leave_group, name='leave_group'),
   path('group/<int:group_id>/request/<int:request_id>/vote/<str:vote>/', views.vote_on_join_request, name='vote_on_join_request'),
]
