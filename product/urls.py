from django.urls import path
from .views import home, add_cart, cart_list

app_name = 'product'

urlpatterns = [
    path('', home, name='list'),
    path('add/<int:id>/', add_cart, name='add-cart'),
    path('cart/list/', cart_list, name='cart-list')
]
