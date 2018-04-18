# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if 'gold_count' not in request.session:
        request.session['gold_count'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    return render(request, 'ninja_app/index.html')

def process_money(request):
    if request.POST['building'] == 'farm':
        earnings = random.randrange(10, 21)
        request.session['gold_count'] += earnings
        string = "You have earned " + str(earnings) + " gold from the farm. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        request.session['activity'].append(string)
    elif request.POST['building'] == 'cave':
        earnings = random.randrange(5, 11)
        request.session['gold_count'] += earnings
        string = "You have earned " + str(earnings) + " gold from the cave. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        request.session['activity'].append(string)
    elif request.POST['building'] == 'house':
        earnings = random.randrange(2, 6)
        request.session['gold_count'] += earnings
        string = "You have earned " + str(earnings) + " gold from the house. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        request.session['activity'].append(string)
    elif request.POST['building'] == 'casino':
        casino_chance = random.randint(1,2)
        earnings = random.randrange(-50, 50)
        request.session['gold_count'] += earnings
        if earnings > 0:
            string = "You have earned " + str(earnings) + " gold from the casino. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
            request.session['activity'].append(string)
        elif earnings < 0:
            string = "You have lost " + str(earnings) + " gold from the casino. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
            request.session['activity'].append(string)
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')

# Create your views here.
