from django.shortcuts import render

# Create your views here.
from shop.models import Item


def items_view(request):
    context = {}
    context["items"] = Item.objects.all()
    return render(request, 'shop.html', context)