from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Person

# Create your views here.
def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people':people})
