from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crypto/', views.crypto_index, name='index'),
    path('crypto/<int:crypto_id>/', views.crypto_detail, name='detail'),

]
