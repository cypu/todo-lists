from django.shortcuts import render, redirect
from lists.models import Item
from django.http import HttpResponse


def home_page(request):
    if request.method == 'POST':
        item = Item()
        item.text = request.POST.get('item_text', '')
        item.save()
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
