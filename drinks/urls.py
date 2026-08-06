from . import views
from django.urls import path

urlpatterns = [
    path('', views.drink_list, name='drink-list'),
    path('<int:id>', views.drink_detail, name='get-drink-by-id'),
]
