from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employes', views.EmployersListToJson, name='EmployersList'),
    path('maxDayOfDate', views.day_of_date, name='day_of_date'),
    path('writeToExcel', views.EmployersListToExcel,name='EmployersListToExel')
]
