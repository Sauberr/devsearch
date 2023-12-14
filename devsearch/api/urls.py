from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.getroutes),
    path('projects/', views.getprojects),
    path('project/<str:pk>/', views.getproject),
    path('project/<str:pk>/vote/', views.projectvote),

    path('remove-tag/', views.removetag)
]