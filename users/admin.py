from django.contrib import admin

from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display=('id','user','image')
    readonly_fields=('id',)
admin.site.register(Profile,ProfileAdmin)
