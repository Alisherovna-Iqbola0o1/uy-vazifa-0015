from django.shortcuts import render, get_object_or_404
from .models import Order
# Create your views here.

def order_list(request):
    orders = Order.objects.all()
    return render(request, "order_list.html", {"orders": orders})


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, "order_detail.html", {"order": order})
