from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.

from app.models import *

def display_topic(request):
    LOT=Topic.objects.all() 
    LOT=Topic.objects.filter(topic_name='cricket')
    d={'topics':LOT}
    return render(request,'display_topic.html',context=d)

def display_webpage(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='BasketBall')
    LOW=Webpage.objects.order_by('-name')
    LOW=Webpage.objects.order_by(Length('name'))
    LOW=Webpage.objects.exclude(name='Abbas')
    d={'webpage':LOW}
    return render(request,'display_webpage.html',d)

def display_access(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.order_by(Length('author').desc())
    LOA=AccessRecord.objects.filter(date__gt='2022-03-16')
    LOA=AccessRecord.objects.filter(date__lt='2022-03-16')
    LOA=AccessRecord.objects.filter(date__gte='2022-03-16')
    LOA=AccessRecord.objects.filter(date__lte='2023-02-16')
    d={'access':LOA}
    return render(request,'display_access.html',d)