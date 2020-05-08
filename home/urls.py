from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    # path("about", views.about, name='about'),
    # path("services", views.services, name='services'),
    # path("contact", views.contact, name='contact'), 
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

