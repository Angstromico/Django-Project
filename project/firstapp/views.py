from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from .forms import ReservationForm

# Create your views here.
def hello_word(request):
    return HttpResponse("Hello World")

class HelloView(View):
    def get(self,request):
        return HttpResponse("Hello World Class Base")

def home(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Reservation created successfully!")
            return redirect('home')
    else:
        form = ReservationForm()
    
    return render(request, 'index.html', {'form': form})