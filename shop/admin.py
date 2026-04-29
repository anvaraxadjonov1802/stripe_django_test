from django.contrib import admin
from django.utils.html import format_html

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "currency", "image_preview")
    list_filter = ("currency",)
    search_fields = ("name", "description")

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit: cover; border-radius: 8px;" />',
                obj.image.url
            )
        return "No image"

    image_preview.short_description = "Preview"