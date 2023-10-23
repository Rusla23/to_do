from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'completed')
    list_filter = ('completed', 'created_at')

admin.site.register(Todo, TodoAdmin)
