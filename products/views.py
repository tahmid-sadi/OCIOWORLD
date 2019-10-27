from django.shortcuts import render
from .models import Chair, Feature


def products_index(request):
    chairs = Chair.objects.all()
    return render(request, 'products/product_introduction.html', {'chairs': chairs})


def details(request):
    return render(request, 'products/product_details.html')



