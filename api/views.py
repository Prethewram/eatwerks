from django.shortcuts import render
from rest_framework import generics,status
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework.response import Response


class AdminLoginView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request, *args, **kwargs):
        serializer = AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response({"detail": "Login successful","id": user.id}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HomePageListCreateView(generics.ListCreateAPIView):
    queryset = HomePageImage.objects.all()
    serializer_class = HomePageSerializer

class HomePageUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomePageImage.objects.all()
    serializer_class = HomePageSerializer

class AboutUsListCreateView(generics.ListCreateAPIView):
    queryset = AboutUsImage.objects.all()
    serializer_class = AboutUsImageSerializer

class AboutUsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutUsImage.objects.all()
    serializer_class = AboutUsImageSerializer

class FoodMenuListCreateView(generics.ListCreateAPIView):
    queryset = FoodMenu.objects.all()
    serializer_class = FoodMenuSerializer

class FoodMenuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodMenu.objects.all()
    serializer_class = FoodMenuSerializer

@api_view(['GET'])
def food_menu_by_type(request, food_type):
    if food_type.upper() not in ['VEG', 'NON_VEG']:
        return Response({'error': 'Invalid food type'}, status=400)

    food_menus = FoodMenu.objects.filter(food_type=food_type.upper())
    serializer = FoodMenuSerializer(food_menus, many=True)
    return Response(serializer.data)

class ChefListCreateView(generics.ListCreateAPIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer

class ChefDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer

class TestimonialListCreateView(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class TestimonialDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer