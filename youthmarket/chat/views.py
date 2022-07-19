# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'index.html', {})

def room(request, room_info):
    # room_info_list = room_info.split('&') # [post_idx, sellerIdx.idx, myInfo.idx]
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_info))
    })
# def chat(request, post_id):
#     return render(request, 'chat.html', {
#         'chat_room_json': mark_safe(json.dumps(post_id))
#     })