from django.shortcuts import render
from django.http import HttpResponse
# Create your views decode
def home_page(request):
	return render(request,'home.html')