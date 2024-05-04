from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView 
from django.urls import path

from .views import UserAPI, TransferAPI

router = DefaultRouter()
router.register('users', UserAPI, basename='api_user')
router.register('transfers', TransferAPI, basename='api_transfer')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh')
]

urlpatterns += router.urls