from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm

# Create your views here.
def hello_word(request):
    return HttpResponse("Hello World")

class HelloView(View):
    def get(self,request):
        return HttpResponse("Hello World Class Base")

def home(request):
    form = ReservationForm()
    if(request.method == 'POST'):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Reservation created successfully!")
    
    return render(request, 'index.html', {'form': form})