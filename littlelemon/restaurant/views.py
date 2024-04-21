from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import generics
from .models import booking, menu
from .serializers import bookingSerializer, menuSerializer, MenuItemSerializer

class bookingView(APIView):
    def get(self, request):
        items= booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data) # Return the serialized JSON data
    
class BookingViewSet(ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = bookingSerializer

class menuView(APIView):
    def post(self, request):
        serializer = menuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})

class MenuItemsView(generics.ListCreatAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuItemSerializer