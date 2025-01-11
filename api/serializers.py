from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageImage
        fields = ['id', 'image']


class AboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsImage
        fields = ['id', 'image']

    
class FoodMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodMenu
        fields = ['id', 'name', 'ingredients', 'image', 'food_type']

class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = ['id', 'name', 'details', 'image']

class TestimonialSerializer(serializers.ModelSerializer):
    proffession = serializers.CharField()
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'proffession' , 'photo' , 'Description']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'icon']

class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_superuser:
                    raise serializers.ValidationError("User does not have admin privileges.")
                data['user'] = user
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")

        return data