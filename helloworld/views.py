from django.shortcuts import render
from django.http import HttpResponse
import time
from ipware.ip import get_real_ip

def index(request):
    ip = (get_real_ip(request))
    return HttpResponse("Helloworld!   " + time.strftime("%c") + "---Your IP Address is " + ip)