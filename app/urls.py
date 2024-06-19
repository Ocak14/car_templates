from django.urls import path
from .views import home_view, testimonial_view, contact_view, team_view, service_view, booking_view, about_view, error_404_view

urlpatterns = [
    path('', home_view, name='home-page'),
    path('about/', about_view, name='about-page'),
    path('contact/', contact_view, name='contact-page'),
    path('team/', team_view, name='team-page'),
    path('testimonial/', testimonial_view, name='testimonial-page'),
    path('service/', service_view, name='service-page'),
    path('booking/', booking_view, name='booking-page'),
    path('404/', error_404_view, name='404-page'),
]
