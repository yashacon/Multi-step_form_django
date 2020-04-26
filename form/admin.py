from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display=('Customer','Basic','Electrical','Mechanical','Installation','Water',)
    list_display_links=['Customer']
    search_fields=['Customer']
    list_per_page=10


admin.site.register(data,CustomerAdmin)
