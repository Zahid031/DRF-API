from django.contrib import admin

# Register your models here.
from .models import House
class HouseAdmin(admin.ModelAdmin):
    #list_display=('id','name','image','manager','points','completed_tasks_count','pending_tasks_count')
    readonly_fields=('id','created_on')

admin.site.register(House,HouseAdmin)