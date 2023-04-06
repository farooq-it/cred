from django.shortcuts import render

# Create your views here.

from app.models import *

def display_topic(request):
    LOT=Topic.objects.all() 
    d={'topics':LOT}
    return render(request,'display_topic.html',context=d)

def display_webpage(request):
    LOW=Webpage.objects.all()
    d={'webpage':LOW}
    return render(request,'display_webpage.html',d)

def display_access(request):
    LOA=AccessRecord.objects.all()
    d={'access':LOA}
    return render(request,'display_access.html',d)