from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.registeruser, name='register'),

    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userprofile, name='user-profile'),
    path('account/', views.useraccount, name='account'),

    path('edit-account/', views.editaccount, name='edit-account'),

    path('create-skill/', views.createskill, name='create-skill'),
    path('update-skill/<str:pk>/', views.updateskill, name='update-skill'),
    path('delete-skill/<str:pk>/', views.deleteskill, name='delete-skill'),

    path('inbox/', views.inbox,  name='inbox'),
    path('message/<str:pk>/', views.viewmessage,  name='message'),
    path('create-message/<str:pk>/', views.createmessage,  name='create-message'),
]