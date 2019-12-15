from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
from shop.models import Item


def items_view(request):
    context = {"items": Item.objects.all()}
    return render(request, 'shop.html', context)

class ShopView(ListView):
    model = Item
    paginate_by = 4
    template_name = 'shop.html'

    def get_queryset(self):
        category = self.request.GET.get('category', 'All')
        sort_order = self.request.GET.get('orderby', 'title')

        if category == 'All':
            return Item.objects.all().order_by(sort_order)
        else:
            return Item.objects.filter(category=category).order_by(sort_order)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = [("All", "All")]
        context['categories'].extend(Item.CATEGORY_CHOICES)
        context['current_category'] = self.request.GET.get('category', 'All')

        context['sort_orders'] = [
            ('title', 'Title'),
            ('category', 'Category'),
            ('price', 'Price'),
            ('rating', 'Rating')
        ]
        context['current_sort_order'] = self.request.GET.get('orderby', 'title')
        return context