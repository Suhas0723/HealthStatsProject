from django.shortcuts import render
from django.http import HttpResponse
import requests
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    response = requests.get("https://health-api.hscc-atlanta.com/v2/patients")
    data = response.json()
    patients = data.get("patients")
    context = {"patients":patients}

    return render(request, "patientsList.html", context)


    return  HttpResponse('HEALTH_MONITOR')

def patient(request, id):
    response = requests.get("https://health-api.hscc-atlanta.com/v2/patient/%s", id)
    data = response.json()
    context = {}
    context["patient_id"] = id
    return render(request, "patient.html", context)

def heartRate(request, id):
    response = requests.get("https://health-api.hscc-atlanta.com/v2/patient/%s/hr", id)
    data = response.json()
    context = {}
    context["name"] = "heart-rate"
    context["value"] = data.get("value")
    return render(request, "heartRate.html", context)

def bloodPressure(request, id):
    response = requests.get("https://health-api.hscc-atlanta.com/v2/patient/%s/bp", id)
    data = response.json()
    data = data.get("value")
    context = {}
    context["name"] = "blood-pressure"
    context["dia"] = data.get("dia")
    context["sys"] = data.get("sys")
    return render(request, "bloodPressure.html", context)

def bloodOxygen(request, id):
    response = requests.get("https://health-api.hscc-atlanta.com/v2/patient/%s/box", id)
    data = response.json()
    context = {}
    context["name"] = "blood-oxygen"
    context["value"] = data.get("value")
    return render(request, "bloodOxygen.html", context)

def temperature(request, id):
    response = requests.get("https://health-api.hscc-atlanta.com/v2/patient/%s/temp", id)
    data = response.json()
    context = {}
    context["name"] = "temperature"
    context["value"] = data.get("value")
    return render(request, "temperature.html", context)
    
    
    
