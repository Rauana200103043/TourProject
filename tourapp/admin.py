from django.contrib import admin
from .models import *
# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname')
    list_display_links = ('id', 'name', 'surname')


admin.site.register(Users, UsersAdmin)
