from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Car

@admin.register(Car)
class EmployeeAdmin(ImportExportModelAdmin):
    pass
# Register your models here.
