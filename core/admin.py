from django.contrib import admin
from .models import User,Position
# Register your models here.
@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['name','emp_code','mobile', 'email', 'desig']

@admin.register(Position)
class PositionModelAdmin(admin.ModelAdmin):
    list_display = ['title']
