from django.shortcuts import render
from matplotlib.style import context
from .models import Item
# Create your views here.


def item_list(request):

    context={
        "item":Item.objects.all()
    }
    h='hello'
    return render(request, h)