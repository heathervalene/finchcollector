from django.contrib import admin

# Register your models here.

from  .models import Finch, Sighting

admin.site.register(Finch)
admin.site.register(Sighting)
