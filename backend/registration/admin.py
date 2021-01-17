from django.contrib import admin
from .models import Registration


# class registrationAdmin(admin.ModelAdmin):
# 	list_display = ('name', 'email_id', 'phone_number')


admin.site.register(Registration)