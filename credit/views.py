from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Client, Account, Credit


class ClientListView(ListView):
    model = Client
    template_name = 'index.html'
    context_object_name = 'clients'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'detail.html'
    context_object_name = 'client'
    pk_url_kwarg = 'client_id'