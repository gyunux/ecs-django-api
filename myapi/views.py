import socket
from django.http import JsonResponse

def load_balance_test(request):

    container_id = socket.gethostname()
    response_data = {
        "message": "Load Balancing Test Success!",
        "handled_by": container_id
    }

    return JsonResponse(response_data)