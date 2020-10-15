from django.urls import path
from . import views
from .views import ListView, ListDetailView, ListCreateView, ListUpdateView, ListDeleteView

urlpatterns = [
    path('', ListView.as_view(), name='TodoList-home'),
    path('list/<int:pk>/', ListDetailView.as_view(), name='list-detail'),
    path('list/new/', ListCreateView.as_view(), name='list-create'),
    path('list/<int:pk>/update/', ListUpdateView.as_view(), name='list-update'),
    path('list/<int:pk>/delete/', ListDeleteView.as_view(), name='list-delete'),
] 
