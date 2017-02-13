from django.contrib import admin

# Register your models here.

from .models import Journal, Entry, Record

admin.site.register(Journal)
admin.site.register(Entry)
admin.site.register(Record)
