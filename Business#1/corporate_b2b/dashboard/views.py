from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from orders.models import Order

@login_required
def dashboard_view(request):
    recent_orders = Order.objects.filter(user=request.user).order_by('-created_at')[:5]
    context = {
        'recent_orders': recent_orders
    }
    return render(request, 'dashboard/home.html', context)