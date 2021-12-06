from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.forms import FeedingForm
from .models import Toad, Toy

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def toads_index(request):
  toads = Toad.objects.all()
  return render(request, 'toads/index.html', {'toads': toads,})

def toads_detail(request, toad_id):
    toad = Toad.objects.get(id=toad_id)
    toys_toad_doesnt_have = Toy.objects.exclude(id__in = toad.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'toads/detail.html', {
      'toad': toad, 'feeding_form': feeding_form,
      'toys': toys_toad_doesnt_have
    })

def add_feeding(request, toad_id):
  # create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the toad_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.toad_id = toad_id
    new_feeding.save()
  return redirect('detail', toad_id=toad_id)

def assoc_toy(request, toad_id, toy_id):
  Toad.objects.get(id=toad_id).toys.add(toy_id)
  return redirect('detail', toad_id=toad_id)

class ToadUpdate(UpdateView):
  model = Toad
  fields = ['breed', 'description', 'age']

class ToadDelete(DeleteView):
  model = Toad
  success_url = '/toads/'

class ToadCreate(CreateView):
  model = Toad
  fields = '__all__'
  success_url = '/toads/'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'
