from django.contrib import admin
from .models import (
    Menu,
    Page,
    Ad,
    Site
)


admin.site.register(Menu)
admin.site.register(Page)
admin.site.register(Ad)
admin.site.register(Site)