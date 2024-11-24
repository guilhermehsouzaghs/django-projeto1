from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html',context={
        'includes': {'teste':4,'teste2':5}
    })

def recipe(request,id):
    return render(request, 'recipes/pages/recipe-detail.html')