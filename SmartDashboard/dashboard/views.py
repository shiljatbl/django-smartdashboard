from django.shortcuts import render, redirect
import requests
from .models import Device
from yeelight import Bulb
from django.urls import reverse
from django.http import HttpResponse
import time
#import requests

# Create your views here.


def index(request):
    devices = Device.objects.all()
    

        

    return render(request, 'dashboard/dashboard.html', {'devices': devices})




def toogle_light(request, id):
    devices = Device.objects.all()
    active_bulb = Device.objects.get(id= id)
    

    bulb = Bulb(active_bulb.ip_address)
    bulb.toggle()
    #bulb.turn_off()

    
    status_check = bulb.get_properties()['power']
    if status_check == "off":
        active_bulb.power_status = False
    else:
        active_bulb.power_status = True
    
    
    print(status_check)
    

    active_bulb.save()
    return redirect('/')


def set_red(request, id):
    
    active_bulb = Device.objects.get(id= id)
    

    bulb = Bulb(active_bulb.ip_address)
    bulb.set_rgb(255,0,0)
    #bulb.turn_off()

    
    status_check = bulb.get_properties()['power']
    if status_check == "off":
        active_bulb.power_status = False
    else:
        active_bulb.power_status = True
    
    
    print(status_check)
    

    active_bulb.save()
    return redirect('/')

def set_blue(request, id):
    
    active_bulb = Device.objects.get(id= id)
    

    bulb = Bulb(active_bulb.ip_address)
    bulb.set_rgb(0,0,255)
    #bulb.turn_off()

    
    status_check = bulb.get_properties()['power']
    if status_check == "off":
        active_bulb.power_status = False
    else:
        active_bulb.power_status = True
    
    
    print(status_check)
    

    active_bulb.save()
    return redirect('/')