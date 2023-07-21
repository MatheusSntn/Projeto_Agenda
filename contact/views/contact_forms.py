from typing import Any, Dict
from contact.models import Contact
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact
from contact.forms import ContactForm

def create(request):
    
    if request.method == 'POST':
        print(request.method)
        context = {
            'form': ContactForm(request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context,
        )
    
    print(request.method)
    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context,
    )
    

    
    # if request.method == 'POST':
    #     print()
    #     print(request.method)
    #     print(request.POST.get('first_name'))
    #     print(request.POST.get('last_name'))
    #     print()
    # print(request.method)

    # print(request.method)
    # print(request.POST.get('first_name'))
    # print(request.POST.get('last_name'))

