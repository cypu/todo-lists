from django.shortcuts import render, redirect
from lists.models import Item
from django.http import HttpResponse


def home_page(request):
    if request.method == 'POST':
        item = Item()
        item.text = request.POST.get('item_text', '')
        item.save()
        return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})