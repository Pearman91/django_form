from django.contrib import admin
from .models import Entrepreneur


@admin.register(Entrepreneur)
class MyAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False