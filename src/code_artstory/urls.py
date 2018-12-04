from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from artstory import views

admin.site.site_header = settings.ADMIN_SITE_HEADER
urlpatterns = [
    url(r'^$', views.article, name='article'),
    url(r'^admin/', admin.site.urls),
    url(r'^product/(?P<product_id>[0-9]+)/$', views.product, name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)