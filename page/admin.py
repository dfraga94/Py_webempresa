from django.contrib import admin

from .models import Page

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


# gestna el modelo en el adminustrador
admin.site.register(Page, PageAdmin)
# Register your models here.
