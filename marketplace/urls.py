from django.urls import path
from . import views

app_name = 'marketplace'

urlpatterns = [
    path('', views.product_list, name='list'),
    path('<persian_slug:slug>/', views.product_detail, name='detail'),
]
