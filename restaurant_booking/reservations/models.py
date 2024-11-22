# reservations/models.py
from django.db import models

class Reservation(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    guests = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True)

    def __str__(self):
        return f"Reservation for {self.full_name} on {self.reservation_date} at {self.reservation_time}"
