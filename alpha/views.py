from datetime import datetime
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from alpha.controllers import get_latest_data, store_latest_data
import json

@csrf_exempt
def handle_request(request):
    if request.method == "GET":
        data = get_latest_data()
        return JsonResponse(data, safe=False)
    data = json.loads(request.body)
    response = store_latest_data(data["name"])
    return JsonResponse(response, safe=False)
