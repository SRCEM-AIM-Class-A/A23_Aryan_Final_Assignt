from django.shortcuts import render, redirect
from .models import Item

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Item.objects.create(name=name)
            return redirect('/')
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
