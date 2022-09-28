from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
#from django.http import HttpResponse
from .models import Room


# Create your views here.
#def main(request):
#   return HttpResponse("Hello Ester and Atli")

#This will not only allow vizualize all room but also create
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer