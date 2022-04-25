from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('register/', views.register),
    path('login/', views.login),
    path('about/', views.about),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
