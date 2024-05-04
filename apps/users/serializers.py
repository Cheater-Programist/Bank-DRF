from rest_framework import serializers
import hashlib

from apps.users.models import User, TransfersHistory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 
                  'last_name', 'email', 'created_at')
        
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 
                  'last_name','age', 'password', 'confirm_password')
        
    def validate(self, attrs):
        if len(attrs['password']) < 8:
            raise serializers.ValidationError('Пароль слишком короткий')
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Пароли отличаются")
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class TransfersHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransfersHistory
        fields = ('id', 'from_user', 'to_user', 'amount', 'is_completed')

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransfersHistory
        fields = ('to_user', 'amount')