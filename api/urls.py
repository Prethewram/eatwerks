from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomePageListCreateView.as_view(), name='home-page-list-create'),
    path('home/<int:pk>/', HomePageUpdateDestroyView.as_view(), name='home-page-detail'),
    path('about/', AboutUsListCreateView.as_view(), name='about-us-list-create'),
    path('about/<int:pk>/', AboutUsRetrieveUpdateDestroyView.as_view(), name='about-us-detail'),
    path('food-menus/', FoodMenuListCreateView.as_view(), name='food-menu-list-create'),
    path('food-menus/type/<str:food_type>/', food_menu_by_type, name='food-menu-by-type'),
    path('food-menus/<int:pk>/', FoodMenuDetailView.as_view(), name='food-menu-detail'),
    path('chefs/', ChefListCreateView.as_view(), name='chef-list-create'),
    path('chefs/<int:pk>/', ChefDetailView.as_view(), name='chef-detail'),
    path('testimonials/', TestimonialListCreateView.as_view(), name='testimonial-list-create'),
    path('testimonials/<int:pk>/', TestimonialDetailView.as_view(), name='testimonial-detail'),
    path('services/', ServiceListCreateView.as_view(), name='service-list-create'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('adminlogin/', AdminLoginView.as_view(), name='admin-login'),

]
