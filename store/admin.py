from django.contrib import admin
from .models import Product,order

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'done')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'description')
    list_editable = ('done', )
    list_filter = ('done',)


class orderAdmin(admin.ModelAdmin):
    list_display=['phone']



admin.site.register(order,orderAdmin)
admin.site.register(Product, ProductAdmin)
