from django.shortcuts import render
from django.http import HttpResponse
import time
from ipware.ip import get_real_ip
from .models import PageCount

def index(request):
    pageCount, create = PageCount.objects.get_or_create(page='index')
    pageCount.count += 1
    pageCount.save()
    ip = (get_real_ip(request))
    return HttpResponse("Helloworld!   " + time.strftime("%c") + "   ---Your IP Address is " + ip + "   ---Page count is " + str(pageCount.count))
