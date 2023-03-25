from django.contrib import admin

# Register your models here.

from .models import Link

# Register your models here.


class LinkAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


# gestna el modelo en el adminustrador
admin.site.register(Link, LinkAdmin)