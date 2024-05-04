from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework_simplejwt.authentication import JWTAuthentication


from apps.users.serializers import UserSerializer, UserRegisterSerializer, TransferSerializer, TransfersHistorySerializer
from apps.users.permissions import UserPermission
from apps.users.models import User, TransfersHistory

# Create your views here.
class UserAPI(GenericViewSet,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserRegisterSerializer
        return UserSerializer

    def get_permissions(self):
        if self.request.method in ('DELETE', 'PUT', 'PATCH'):
            return (UserPermission(), )
        return (AllowAny(), )
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        
class TransferAPI(GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin):
    queryset = TransfersHistory.objects.all()
    serializer_class = TransferSerializer
    authentication_classes = [JWTAuthentication]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TransferSerializer
        return TransfersHistorySerializer