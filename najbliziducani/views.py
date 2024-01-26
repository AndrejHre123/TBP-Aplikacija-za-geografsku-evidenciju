from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop
from django.http import JsonResponse
import json


# Create your views here.
latitude = 45.816782
longitude = 16.003975

user_location = Point(longitude, latitude, srid=4326)

# Create your views here.
class Home(generic.ListView):
    model = Shop
    context_object_name="shops"
    queryset = Shop.objects.annotate(distance=Distance("lokacija", user_location)).order_by("distance")[0:5]
    template_name = "ducani/index.html"

def get_nearest_shops(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_lat = data['latitude']
        user_lng = data['longitude']
        user_location = Point(user_lng, user_lat, srid=4326)
        
        nearest_shops = Shop.objects.annotate(distance=Distance("lokacija", user_location)).order_by("distance")[:5]
        
        shops_data = [
    {
        'name': shop.ime, 
        'lat': shop.lokacija.y, 
        'lng': shop.lokacija.x,
        'adresa': shop.adresa,
        'grad': shop.grad,
        'radno_vrijeme': shop.radno_vrijeme,
        'web': shop.web
    } 
    for shop in nearest_shops]
        return JsonResponse({'shops': shops_data})

    return JsonResponse({'error': 'Invalid request'}, status=400)

def tocke_view(request):
    return render(request, 'tocke.html')    