from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from app1.models import *
from django.db.models import Q


# Create your views here.
def index(request):
    Building_name =Building.objects.all()
    context = {
        'B_names': Building_name
    }

    if request.GET.get('name'):
        B_name = request.GET.get('name')
        Check_in = request.GET.get('check_in')
        Check_out = request.GET.get('check_out')

        rooms_data = Room.objects.filter(
            Room_Type__Building__id=B_name,
            Price__gt=0,
        )

        blocked_room_ids = BlockedDay.objects.filter(Day__range=[Check_in, Check_out]).values_list('Room_id',
                                                                                                    flat=True)
        room_queryset = rooms_data.exclude(id__in=blocked_room_ids)

        available_rooms = room_queryset.order_by('Price')
        datas = []
        for room in available_rooms:
            datas.append({
                'room_id': room.Room_Type.Building.Name,
                'room_number': room.Number,
                'room_type': room.Room_Type.Type,
                'room_price': room.Price,
            })
        context = {
            'B_names': Building_name,
            'datas': datas,
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html', context)