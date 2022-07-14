from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crypto/', views.crypto_index, name='index'),
    path('crypto/<int:crypto_id>/', views.crypto_detail, name='detail'),
    path('crypto/create/', views.CryptoCreate.as_view(), name='crypto_create'),
    path('crypto/<int:pk>/update/', views.CryptoUpdate.as_view(), name='crypto_update'),
    path('crypto/<int:pk>/delete/', views.CryptoDelete.as_view(), name='crypto_delete'),

]
