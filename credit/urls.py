from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientListView.as_view()),
    path('<int:client_id>/', views.ClientDetailView.as_view(), name='detail'),
]