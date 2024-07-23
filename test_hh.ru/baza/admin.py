from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from baza.models import FIASNode

# Register your models here.

admin.site.register(FIASNode,MPTTModelAdmin)
