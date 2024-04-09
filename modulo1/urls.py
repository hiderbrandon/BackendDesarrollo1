from django.urls import path
from .views import ObraListCreateView, ObraDetailView,AllObrasListView,ObraDeleteView,ObraUpdateView
from django.urls import path , include

urlpatterns = [
    path('Obras/', ObraListCreateView.as_view(), name='Obra-list-create'),
    path('Obras/<int:pk>/', ObraDetailView.as_view(), name='Obra-detail'),
    path('Obras/all/', AllObrasListView.as_view(), name='all-Obras-list'),  
    path('Obras/delete/<int:pk>/', ObraDeleteView.as_view(), name='Obra-delete'), 
    path('Obras/update/<int:pk>/', ObraUpdateView.as_view(), name='Obra-update'), 
]