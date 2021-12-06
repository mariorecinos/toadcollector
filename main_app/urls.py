from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('toads/', views.toads_index, name='index'),
  path('toads/<int:toad_id>/', views.toads_detail, name='detail'),
  path('toads/create', views.ToadCreate.as_view(), name='toads_create'),
  path('toads/<int:pk>/update/', views.ToadUpdate.as_view(), name='toads_update'),
  path('toads/<int:pk>/delete/', views.ToadDelete.as_view(), name='toads_delete'),
  path('toads/<int:toad_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
  path('toads/<int:toad_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),

]
