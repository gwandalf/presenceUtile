#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	""" Main view : welcoming message """
	text = """ <h1> Tableau des missions !</h1>
              <p>Consultez les missions affichées.</p> """
	return HttpResponse(text)
