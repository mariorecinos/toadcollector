from django.shortcuts import render
from .models import Toad

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'main/home.html')
def about(request):
  return render(request, 'main/about.html')
def toads_index(request):
  toads = Toad.objects.all()
  return render(request, 'toads/index.html', { 'toads': toads })
def toads_detail(request, toad_id):
  toad= Toad.objects.get(id=toad_id)
  return render(request, 'toads/detail.html', { 'toad': toad })
