from .models import Cart

def cart_items(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        return {'cart_items': cart_items}
    return {'cart_items': []}
