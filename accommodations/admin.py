from django.contrib import admin
from .models import Accommodation, AccommodationImage


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'location', 'price_per_night', 'capacity', 'is_available',
                    'get_reservation_count']
    list_filter = ['category', 'is_available', 'created_at']
    search_fields = ['title', 'location', 'description']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['reserved_by']

    def get_reservation_count(self, obj):
        return obj.reserved_by.count()

    get_reservation_count.short_description = 'تعداد رزرو'


@admin.register(AccommodationImage)
class AccommodationImageAdmin(admin.ModelAdmin):
    list_display = ['accommodation', 'image', 'created_at']
    list_filter = ['created_at']
