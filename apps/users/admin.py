from django.contrib import admin
from .models import User, TransfersHistory
# Register your models here.

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['username', 'wallet_address', 'balance']
    
@admin.register(TransfersHistory)
class AdminTransfer(admin.ModelAdmin):
    list_display = ['from_user', 'to_user', 'amount', 'is_completed', 'created_at']