from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView



urlpatterns = [
    path('tweets/', views.index),
    # path('tweets/<str:username>/', views.findTweet),
    path('users/', views.users),
    path('users/<str:username>/', views.findUser),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]