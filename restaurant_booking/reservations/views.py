# reservations/views.py
from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.contrib import messages

def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation successful!')
            return redirect('reservation_success')
        else:
            messages.error(request, 'There was an error with your reservation.')
    else:
        form = ReservationForm()
    
    return render(request, 'reservation_form.html', {'form': form})
