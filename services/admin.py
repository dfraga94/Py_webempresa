from django.contrib import admin

from .models import Service

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


# gestna el modelo en el adminustrador
admin.site.register(Service, ServiceAdmin)