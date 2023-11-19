from django.shortcuts import render, redirect
from base.models import Room  # Adjust the import statement based on the directory structure
from .forms import RoomForm  # Adjust the import statement based on the directory structure


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

def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)  # pylint: disable=no-member
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)  # pylint: disable=no-member
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})
