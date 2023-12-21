import random

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import ProductModel


def home(request):
    products = ProductModel.objects.all()
    return render(request, 'home.html', context={
        'products': products
    })


def add_cart(request, id):
    cart = request.session.get('cart', [])

    if id in cart:
        cart.remove(id)
    else:
        cart.append(id)

    request.session['cart'] = cart
    return redirect('/')


def cart_list(request):
    cart = request.session.get('cart', [])
    products = ProductModel.objects.filter(id__in=cart)
    return render(request, 'cart_list.html', context={
        'products': products
    })
