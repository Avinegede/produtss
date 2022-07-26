from django.contrib import admin
from .models import Product, Producer

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'producer',
                'posted_by',
                'productName',
                'productType',
                'description',
                'amount',
                'price',
                'discount',
            ),
        }),
    )

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'title',
            ),
        }),
    )




