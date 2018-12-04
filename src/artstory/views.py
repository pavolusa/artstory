# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Type, Product, Article, ThumbnailHome
# Create your views here.

def index(request):
    type_objs = Type.objects.filter(active__exact=True)
    context = {
        'type_objs': type_objs,
    }
    return render(request, "artstory/type.html", context)
    
def product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'artstory/product.html', {'product': product})

def article(request):
    type_objs = ThumbnailHome.objects.filter(active__exact=True)
    context = {
        'type_objs': type_objs,
    }
    return render(request, "artstory/index.html", context)

def hello(request):
	name = "Vu"
	html = "<html><body>Hi %s, this seems to have worked!</body></html>" %name
	return HttpResponse(html)