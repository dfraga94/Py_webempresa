
from page.models import Page
from django import template

register=template.Library()

@register.simple_tag
def get_page_list():
    page=Page.objects.all()
    return page