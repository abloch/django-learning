from django.contrib import admin
from finder.models import Business

class BusinessAdmin(admin.ModelAdmin):
    fields = ['name']

# Register your models here.
admin.site.register(Business,BusinessAdmin)
