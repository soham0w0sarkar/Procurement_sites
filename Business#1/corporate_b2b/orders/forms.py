from django import forms
from .models import Order, OrderItem
from products.models import Product

class OrderForm(forms.ModelForm):  # Changed from OrderCreateForm to OrderForm
    class Meta:
        model = Order
        fields = ['status']  # Only expose status to forms

class OrderItemForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        widget=forms.HiddenInput()
    )
    quantity = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control quantity-input',
            'data-price': ''  # Will be set via JavaScript
        })
    )

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

OrderItemFormSet = forms.inlineformset_factory(
    Order,
    OrderItem,
    form=OrderItemForm,
    extra=1,
    can_delete=True
)