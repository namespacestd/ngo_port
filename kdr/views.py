from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
	return render(request, 'index.html')