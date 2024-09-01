from django.shortcuts import render
import random
from .models import Cat

# Create your views here.
def index(request):
    data = {
        'gifs' : 'https://cataas.com/cat/gif',
        'imgs' : 'https://cataas.com/cat?html=true',
    }
    return render(request, 'main/index.html', data)

def about(request):
    data1 = Cat.objects.order_by('-published_at')[:3]
    return render(request, 'main/about.html', {'data1' : data1})