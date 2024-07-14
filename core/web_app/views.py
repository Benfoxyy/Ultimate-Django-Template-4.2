from django.shortcuts import render
from time import sleep
from django.views.decorators.cache import cache_page

# Create your views here.

@cache_page(60 * 15)
def home(request):
    sleep(10)
    return render(request,'index.html')