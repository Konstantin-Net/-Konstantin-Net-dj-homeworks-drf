from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sor = request.GET.get("sort")
    template = 'catalog.html'
    if sor == 'name':
        phones = Phone.objects.all().order_by('name')
        context = {"phones": phones}
        return render(request, template, context)
    elif sor == 'min_price':
        phones = Phone.objects.all().order_by('price')
        context = {"phones": phones}
        return render(request, template, context)
    elif sor == 'max_price':
        phones = Phone.objects.all().order_by('-price')
        context = {"phones": phones}
        return render(request, template, context)
    else:
        phones = Phone.objects.all()
        context = {"phones": phones}
        return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {"phone": phone}
    return render(request, template, context)

