from django.urls import path
from . import views

app_name = 'supercarapp'

urlpatterns = [
    path('',views.index, name='index'),
    #path('',views.IndexClassView.as_view(), name='index')
    path('<int:item_id>/', views.detail, name='detail'),
    path('car/',views.car, name='car'),
    path('add', views.CreateCar, name='CreateCar'),
    path('update/<int:id>/', views.UpdateCar, name='UpdateCar'),
    path('delete/<int:id>/', views.DeleteCar, name='DeleteCar'),
]