from django.shortcuts import render, redirect
from lists.models import Item
from django.http import HttpResponse


def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST.get('item_text', '')
        item = Item()
        item.text = new_item_text
        item.save()
        return redirect('/')
    else:
        new_item_text = ''

    return render(request, 'home.html', {'new_item_text': new_item_text})
