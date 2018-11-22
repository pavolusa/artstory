# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Type, Product, Article, ThumbnailHome

class TypeModelAdmin(admin.ModelAdmin):
    list_filter = ('active',)
    list_display = ('name', 'active', )

class ProductModelAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)    
    list_display = ('name', 'price', 'quantity', 'description')

class ArticleModelAdmin(admin.ModelAdmin):
    list_filter = ('active',)
    list_display = ('name', 'active', 'description')

class ThumbnailHomeModelAdmin(admin.ModelAdmin):
    list_filter = ('active',)
    list_display = ('name', 'active', 'image')

admin.site.register(Type, TypeModelAdmin)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(Article, ArticleModelAdmin)
admin.site.register(ThumbnailHome, ThumbnailHomeModelAdmin)