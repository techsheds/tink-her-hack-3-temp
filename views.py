from django.shortcuts import render,redirect
from .models import Donor
from .forms import DonorForm  # Make sure you have imported your form


def home(request):
    donors= Donor.objects.all()
    return render(request, 'home.html',{'donors':donors})
def donor_list(request):
    blood_group=request.GET.get('blood_group')
    city=request.GET.get('city')
    donors=Donor.objects.all()
    if blood_group:
        donors =donors.filter(blood_group=blood_group)
    if city:
        donors=donors.filter(city__icontains=city)    
    return render(request,'donors.html',{'donors':donors})

def donate_view(request):
    form=DonorForm()
    if request.method == 'POST':
        form = DonorForm(request.POST)  # Form will be bound with POST data
        if form.is_valid():
            # Save form or process the data here
            form.save()
            return redirect('home')# Create an empty form for GET request

    return render(request, 'donation.html', {'form': form})  # Make sure you always pass 'form'
