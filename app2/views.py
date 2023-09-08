from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vista2(request):
    html="""
    <h1>Vista dos</h1>
    """
    return HttpResponse(html)