from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ksiazki/', views.KsiazkaListView.as_view(), name='ksiazki'),
    path('autorzy/', views.AutorListView.as_view(), name='autorzy'),
]
