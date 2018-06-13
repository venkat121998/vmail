from django.contrib import admin

# Register your models here.
from .models import vmailuser,Vmails
admin.site.register(vmailuser)
admin.site.register(Vmails)