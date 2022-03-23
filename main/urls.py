from django.urls import path

from .views import *

urlpatterns = [
    path('create/', CreateProductView.as_view(), name='create-product'),
    path('<slug:category_id>/', ProductsListView.as_view(), name='products-list'),
    path('details/<int:pk>/', ProductDetailsView.as_view(), name='product-details'),
    path('update/<int:pk>/', UpdateProductView.as_view(), name='update-product'),
    path('delete/<int:pk>/', DeleteProductView.as_view(), name='delete-product')
]
