# restaurant_booking/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reservations.urls')),  # Include URLs from the reservations app
]