from django.contrib import admin

# Register your models here.
from myApp.models import Student

class StudentAdmin(admin.ModelAdmin):
    l=['sno','sname','smarks','saddr']

admin.site.register(Student,StudentAdmin)