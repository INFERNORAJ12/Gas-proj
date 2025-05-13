from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from customers.models import ServiceRequest

@staff_member_required
def request_list(request):
    requests = ServiceRequest.objects.all().order_by('-submitted_on')
    return render(request, 'support/request_list.html', {'requests': requests})

@staff_member_required
def update_request(request, request_id):
    sr = get_object_or_404(ServiceRequest, pk=request_id)
    if request.method == 'POST':
        sr.status = request.POST['status']
        if sr.status == 'resolved':
            from django.utils import timezone
            sr.resolved_on = timezone.now()
        sr.save()
        return redirect('support_list')
    return render(request, 'support/update_request.html', {'sr': sr})