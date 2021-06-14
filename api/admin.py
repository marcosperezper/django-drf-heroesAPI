from django.contrib import admin

# Register your models here.
from .models import Hero


class HeroAdmin(admin.ModelAdmin):
    search_fields = ("name__icontains",)
    list_display = ("alias", "name")


admin.site.register(Hero, HeroAdmin)
