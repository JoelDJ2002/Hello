from dataclasses import fields
from django.contrib import admin
from home.models import Contact
# Register your models here.

class Snip(admin.ModelAdmin):
    list_display =  ('name', 'phone', 'email')
admin.site.register(Contact, Snip)

