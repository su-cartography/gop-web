from django.contrib import admin
from .models import Icon, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Icon)
class IconAdmin(admin.ModelAdmin):
    list_display = ("unique_id", "primary_tag", "designer", "status", "updated_at")
    list_filter = ("status",)
    search_fields = ("unique_id", "primary_tag", "designer", "uploader", "icon_description")
    filter_horizontal = ("tags",)