from django.urls import path
from . import views

app_name = 'tours'

urlpatterns = [
    # fixed paths must come BEFORE the <persian_slug:slug>/ catch-all
    path('my/reservations/', views.my_reservations, name='my_reservations'),
    path('', views.tour_list, name='list'),
    path('<persian_slug:slug>/', views.tour_detail, name='detail'),
    path('<persian_slug:slug>/reserve/', views.reserve_tour, name='reserve'),
    path('<persian_slug:slug>/cancel/', views.cancel_reservation, name='cancel_reservation'),
]
