from django.shortcuts import render, redirect
from .models import Device
from yeelight import Bulb
from django.urls import reverse
from django.http import HttpResponse
import time
# Create your views here.


def index(request):
    devices = Device.objects.all()
    
    

    return render(request, 'dashboard/dashboard.html', {'devices': devices})


def toogle_light(request, id):
    devices = Device.objects.all()
    active_bulb = Device.objects.get(id= id)
    

    bulb = Bulb(active_bulb.ip_address)
    bulb.turn_off()
    time.sleep(1)
    bulb.turn_on()

    if active_bulb.power_status == False:
        active_bulb.power_status = True
    else:
        active_bulb.power_status = False

    active_bulb.save()
    return redirect('/')