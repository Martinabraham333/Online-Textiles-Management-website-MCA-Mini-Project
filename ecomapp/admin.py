from django.contrib import admin
from .models import *

class jobapp(admin.ModelAdmin):
    list_display= ('user','phonenumber','Experiencs','file')
admin.site.register(
    [Admin, Customer, Category, Product, Cart, CartProduct, Order, ProductImage])
admin.site.register(jobapplication,jobapp)

admin.site.register(workdetails)
admin.site.register(tailor)
