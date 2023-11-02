from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index),
    path('home/',views.home)
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
