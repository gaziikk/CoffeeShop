from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from index_page.views import index, add_special, add_chef, admin_menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('add_special/', add_special, name='add_special'),
    path('add_chef/', add_chef, name='add_chef'),
    path('admin_menu/', admin_menu, name='admin_menu'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404_view
