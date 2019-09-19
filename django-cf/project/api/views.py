from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
from .models import Message
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
import json


@require_http_methods(['GET'])
def get_messages(request):
    data = list(Message.objects.all().values())
    return JsonResponse({"data": data})


@csrf_exempt
@require_http_methods(['POST'])
def add_message(request):
    try:
        data = json.loads(request.body)
        new_msg = Message(**data)
        new_msg.save()
        return JsonResponse(model_to_dict(new_msg), status=201)
    except Exception as ex:
        return JsonResponse({"error", ex}, status=500, safe=False)


@csrf_exempt
@require_http_methods(['DELETE'])
def delete_message(request):
    try:
        data = json.loads(request.body)
        msg_to_delete = Message(id=data["id"])
        Message.objects.filter(id=data["id"]).delete()
        return JsonResponse(model_to_dict(msg_to_delete), status=201)
    except Exception as ex:
        return JsonResponse({"error", ex}, status=500, safe=False)


@csrf_exempt
@require_http_methods(['PUT'])
def update_message(request, id):
    try:
        data = json.loads(request.body)
        msg_to_update = Message(id=id)
        Message.objects.filter(id=id).update(text=data['text'])
        return JsonResponse(model_to_dict(msg_to_update), status=201)
    except Exception as ex:
        return JsonResponse({"error", ex}, status=500, safe=False)
