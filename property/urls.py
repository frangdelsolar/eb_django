from django.urls import path

from .views import PropertyListView, PropertyDetailView


urlpatterns = [
    path('', PropertyListView.as_view(), name='property-list'),
    path('<str:id>/', PropertyDetailView.as_view(), name='property-detail')
]
