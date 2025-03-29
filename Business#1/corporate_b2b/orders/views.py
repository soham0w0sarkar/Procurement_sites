from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from .forms import OrderForm, OrderItemFormSet
from products.models import Product

@login_required
def order_list(request):
    """Display all orders for the current user"""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/list.html', {'orders': orders})

@login_required
def order_create(request):
    """Create a new order"""
    if request.method == 'POST':
        form = OrderForm(request.POST)
        formset = OrderItemFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            formset.instance = order
            formset.save()
            return redirect('orders:detail', pk=order.pk)
    else:
        form = OrderForm()
        formset = OrderItemFormSet()
    
    return render(request, 'orders/create.html', {
        'form': form,
        'formset': formset
    })

@login_required
def order_detail(request, pk):
    """View order details"""
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'orders/detail.html', {'order': order})

@login_required
def order_edit(request, pk):
    """Edit an existing order"""
    order = get_object_or_404(Order, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        formset = OrderItemFormSet(request.POST, instance=order)
        
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('orders:detail', pk=order.pk)
    else:
        form = OrderForm(instance=order)
        formset = OrderItemFormSet(instance=order)
    
    return render(request, 'orders/edit.html', {
        'form': form,
        'formset': formset,
        'order': order
    })