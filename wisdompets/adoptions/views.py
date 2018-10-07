from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<p>home view</p>')

def pet_detail(request, id):
    return HttpResponse('<p>pet_detail view wtih the id {}</p>'.format(id))

def forms_template(request):
    return render(request, 'forms.html')
