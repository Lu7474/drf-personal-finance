from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView

urlpatterns = [
    # Регистрация
    path("register/", RegisterView.as_view(), name="auth_register"),
    # Логин (получение токена)
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # Обновление токена (refresh)
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
