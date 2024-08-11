from django.http import JsonResponse
from django.shortcuts import render
from .models import RadarEntry


def home(request):
    return render(request, 'index.html')

def radar_view(request):
    radar_entries = RadarEntry.objects.all()
    context = {
        radar_entries: radar_entries
    }
    return render(request, 'index.html', context)

def radar_entries_view(request):
    entries = RadarEntry.objects.all().values('label', 'quadrant', 'ring', 'moved')
    return JsonResponse(list(entries), safe=False)