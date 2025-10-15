from django.contrib import admin
from django.utils.html import format_html
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_description', 'image_preview', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    def short_description(self, obj):
        """Matnni qisqartirib ko‘rsatadi."""
        return (obj.description[:60] + '...') if len(obj.description) > 60 else obj.description
    short_description.short_description = 'Description'

    def image_preview(self, obj):
        """Rasmni kichik holatda admin ro‘yxatida ko‘rsatadi."""
        if obj.image:
            return format_html('<img src="{}" width="80" style="border-radius:6px"/>', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image'
