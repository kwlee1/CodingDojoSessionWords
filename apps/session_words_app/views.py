# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from time import strftime

def index(request):
    if 'fullsession' not in request.session:
        request.session['fullsession'] = []
    print request.session['fullsession']
    return render(request, 'index.html')


def input(request):
    print request.session['fullsession']
    if request.POST['word'] != "":
        if 'bigfonts' in request.POST: 
            if request.POST['color'] == 'red':
                newentry = {
                    'word': request.POST['word'],
                    'class': 'red bold',
                    'created_at': strftime('%B %d %Y %X')
                }
                my_list = request.session['fullsession']
                my_list.append(newentry)
                request.session['fullsession'] = my_list
            if request.POST['color'] == 'green':
                newentry = {
                    'word': request.POST['word'],
                    'class': 'green bold',
                    'created_at': strftime('%B %d %Y %X')
                }
                my_list = request.session['fullsession']
                my_list.append(newentry)
                request.session['fullsession'] = my_list
            if request.POST['color'] == 'blue':
                newentry = {
                    'word': request.POST['word'],
                    'class': 'blue bold',
                    'created_at': strftime('%B %d %Y %X')
                }
                my_list = request.session['fullsession']
                my_list.append(newentry)
                request.session['fullsession'] = my_list
        else: 
            if request.POST['color'] == 'red':
                newentry = {
                    'word': request.POST['word'],
                    'class': 'red',
                    'created_at': strftime('%B %d %Y %X')
                }
                my_list = request.session['fullsession']
                my_list.append(newentry)
                request.session['fullsession'] = my_list
            if request.POST['color'] == 'green':
                newentry = {
                    'word': request.POST['word'],
                    'class': 'green',
                    'created_at': strftime('%B %d %Y %X')
                }
                my_list = request.session['fullsession']
                my_list.append(newentry)
                request.session['fullsession'] = my_list
            if request.POST['color'] == 'blue':
                newentry = {
                    'word': request.POST['word'],
                    'class': 'blue',
                    'created_at': strftime('%B %d %Y %X')
                }
                my_list = request.session['fullsession']
                my_list.append(newentry)
                request.session['fullsession'] = my_list

    print request.session['fullsession']
    return redirect('/')

def clear(request):
    my_list = []
    request.session['fullsession'] = my_list
    return redirect('/')