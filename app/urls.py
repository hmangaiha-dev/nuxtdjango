from django.urls import path
from .views import PostView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh_token/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('posts/',PostView.as_view(),name="posts_view"),
]
