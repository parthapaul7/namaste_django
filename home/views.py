from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required 
# Create your views here.
@login_required(login_url="/admin")
def home(request):
    return render(request, 'home/welcom.html',{"time":datetime.now()}) 
