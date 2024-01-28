from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.

def main(request):
    return HttpResponse("Hello")
    
def get_eonet_events(request):
    url = "https://eonet.gsfc.nasa.gov/api/v3/events"
    params = {
        "status": "open",
        "limit": 20
    }
    response = requests.get(url, params=params)
    events = response.json().get('events', [])
    
    return render(request, 'eventsTest.html', {'events': events})