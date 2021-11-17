from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('toads/', views.toads_index, name='index'),
    path('toads/<int:toad_id>/', views.toads_detail, name='detail'),
]
