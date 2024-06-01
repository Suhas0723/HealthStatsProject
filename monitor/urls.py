from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('patient/<id>', views.patient, name = 'patient'),
    path('patient/heart-rate/<id>', views.heartRate, name = 'heartRate'),
    path('patient/blood-pressure/<id>', views.bloodPressure, name = 'bloodPressure'),
    path('patient/blood-oxygen/<id>', views.bloodOxygen, name = 'bloodOxygen'),
    path('patient/temperature/<id>', views.temperature, name = 'temperature'),
    path('patients', views.temperature, name = 'temperature'),
    
]