from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Car
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .forms import CarForm
from django.views.generic.list import ListView
# Create your views here.

def index(request):
    CarList = Car.objects.all().order_by("-id")
    context = {
        'CarList': CarList,
    }
    return render(request,'supercarapp/index.html', context)

class IndexClassView(ListView):
    model = Car
    template_name = 'supercarapp/index.html'
    context_object_name = 'CarList'



def car(request):
    return HttpResponse('<h1>This is an item view</h1>')

def detail(request, item_id):
    car = Car.objects.get(pk=item_id)
    context = {
        'Car':car,
    }

    return render(request, 'supercarapp/detail.html', context)

def CreateCar(request):
    form = CarForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('supercarapp:index')
    return render(request,'supercarapp/Car-form.html', {
        'form':form
    })

def UpdateCar(request, id):
    car = Car.objects.get(id=id)
    form = CarForm(request.POST or None, instance=car)

    if form.is_valid():
        form.save()
        return redirect('supercarapp:index')
    return render(request, 'supercarapp/Car-form.html', {
        'form':form,
        'car':car
    })

def DeleteCar(request,id):
    car = Car.objects.get(id=id)

    if request.method == 'POST':
        car.delete()
        return redirect('supercarapp:index')
    return render(request,'supercarapp/Car-delete.html', {
        'car':car
    })