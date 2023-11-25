from django.shortcuts import render, redirect
from chat_app.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from urllib.parse import urlencode


def home_view(request):
    return render(request, 'home.html')


def room(request):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)  # gets the partical model that has the name of this room
    return render(request, 'room.html',
                  {"username": username, "room": room, "room_details": room_details})


def checkview(request):
    room_name = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room_name+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room_name+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    #
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Your message sent successfully!')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
