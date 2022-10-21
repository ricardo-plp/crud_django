from django.shortcuts import render

# Create your views here.
from .models import Questions


def index(request):
    questions = Questions.objects.all()
    return render(request, 'app/index.html',{'questions':questions})