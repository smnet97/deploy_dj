from django import template

register = template.Library()


@register.simple_tag
def count_cart(request):
    cart = request.session.get('cart', [])
    return len(cart)


@register.simple_tag
def check_cart(request, product_id: int):
    cart = request.session.get('cart', [])
    return product_id in cart
