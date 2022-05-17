from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User


@login_required
def index(request):
    print(request.user)
    all_user = User.objects.all()
    print(all_user)
    return render(request, 'chat/index.html', {'users': all_user})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
