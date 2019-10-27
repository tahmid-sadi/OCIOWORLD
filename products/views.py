from django.shortcuts import render


def products_index(request):
    return render(request, 'products/product_introduction.html')


def details(request):
    return render(request, 'products/product_details.html')



