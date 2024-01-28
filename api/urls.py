from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('events/', views.get_eonet_events, name='eonet-events'),
]
