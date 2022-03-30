from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView

from main.models import Product
from .forms import AddToCartForm, CheckoutForm
from .models import Cart, Order, OrderItems


class AddToCartView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart = Cart(request)
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data.get('quantity')
            cart.add(product.id, quantity, str(product.price))
        return redirect(reverse_lazy('cart-details'))


class RemoveFromCartView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product_id)
        return redirect(reverse_lazy('cart-details'))


class CartDetailsView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'order/cart_details.html', {'cart': cart})


class IncrementQuantityView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.increment_quantity(product_id)
        return redirect(reverse_lazy('cart-details'))


class PlaceOrderView(LoginRequiredMixin, View):
    template_name = 'order/checkout.html'
    form_class = CheckoutForm

    def get(self, request):
        form = self.form_class()
        cart = Cart(request)
        return render(request, self.template_name, {'form': form,
                                                    'cart': cart})

    def post(self, request):
        user = request.user
        cart = Cart(request)
        form = self.form_class(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            address = form.cleaned_data.get('address')
            order = Order.objects.create(user=user,
                                         phone_number=phone_number,
                                         address=address,
                                         status='open')
            for item in cart:
                OrderItems.objects.create(order=order,
                                          product=item['product'],
                                          quantity=item['quantity'])
            cart.clear()
            return redirect(reverse_lazy())


class OrdersListView(LoginRequiredMixin, ListView):
    pass
