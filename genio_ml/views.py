from random import random
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello, world! This is the Genio ML app.</h1>")

def get_data(request):
    data = {
        "name": "Genio ML",
        "description": "A machine learning application for Genio Hub.",
        "version": "1.0.0"
    }
    return JsonResponse(data)

def random_number(request):
    number = int(random() * 100)  # Generate a random number between 0 and 100
    return JsonResponse({"random_number": number})