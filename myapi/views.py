import socket
from django.http import JsonResponse
from .models import Product

def product_list(request):

    container_id = socket.gethostname()
    data = {
        "handled_by": container_id
    }

    return JsonResponse(data)