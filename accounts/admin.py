from django.contrib import admin

from .models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name')
    list_per_page = (5)