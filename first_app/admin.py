from django.contrib import admin
from .models import Company, Product, Order


# class OrderAdmin(admin.ModelAdmin):
#     model = Order
#     list_display = ('company', 'product', 'quantity',)
#
#     def get_order(self):
#         return self.generate_order_number


admin.site.register(Company)
admin.site.register(Product)
admin.site.register(Order)
