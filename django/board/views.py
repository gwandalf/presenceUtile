#-*- coding: utf-8 -*-
from django.shortcuts import render
from datetime import datetime
from models import Mission

# Create your views here.


def home(request):
    """ Main view : list of missions """
    missions = Mission.objects.all()
    return render(request, 'board/board.html', {'missions': missions})
