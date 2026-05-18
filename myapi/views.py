import socket
from django.http import JsonResponse
from .models import Product

def product_list(request):

    products = Product.objects.all()
    container_id = socket.gethostname()
    data = {
        {   "handled_by" : container_id,
            "name": product.name,"price" : product.price}
        for product in products
    }

    return JsonResponse(data)