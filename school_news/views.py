from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    contextDictionary = {'display': 'header, main, footer'}

    return render(request, 'template/index.html', context=contextDictionary)
