from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "full_name", "is_staff", "date_joined")
    search_fields = ("email", "full_name")