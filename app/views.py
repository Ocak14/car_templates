from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def team_view(request):
    return render(request, 'team.html')

def testimonial_view(request):
    return render(request, 'testimonial.html')

def service_view(request):
    return render(request, 'service.html')

def booking_view(request):
    return render(request, 'booking.html')

def error_404_view(request, exception):
    return render(request, '404.html', status=404)
