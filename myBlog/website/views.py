from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html", 
                {"current_time": datetime.now()})