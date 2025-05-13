from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest

@login_required
def dashboard(request):
    requests = ServiceRequest.objects.filter(customer=request.user).order_by('-submitted_on')
    return render(request, 'customers/dashboard.html', {'requests': requests})

@login_required
def new_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('dashboard')
    else:
        form = ServiceRequestForm()
    return render(request, 'customers/new_request.html', {'form': form})