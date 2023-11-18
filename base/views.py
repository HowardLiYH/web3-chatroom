from django.shortcuts import render
from base.models import Room  # Adjust the import statement based on the directory structure

# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Lets talk about Bitcoin'},
#     {'id': 2, 'name': 'NFT Collector Playground'},
#     {'id': 3, 'name': 'Technical Analysis Education'},
# ]


def home(request):
    rooms = Room.objects.all()  # pylint: disable=no-member
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)  # pylint: disable=no-member
    context = {'room': room}
    return render(request, 'base/room.html', context)
