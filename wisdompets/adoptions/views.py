from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.http import Http404

from .models import Pet

# Create your views here.
def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets': pets})
    # return HttpResponse('<p>home view</p>')

def pet_detail(request, id):
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'pet_detail.html')
    # return HttpResponse('<p>pet_detail view wtih the id {}</p>'.format(id))

def forms_template(request):
    return render(request, 'forms.html')
