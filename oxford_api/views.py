from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

BASE_URL = 'https://od-api.oxforddictionaries.com/api/v1'


def search(request):
    """The search view."""
    return HttpResponse('At the index page.')