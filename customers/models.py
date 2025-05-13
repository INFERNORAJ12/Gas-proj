from django.contrib.auth.models import User
from django.db import models

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('gas_leak', 'Gas Leak'),
        ('installation', 'New Installation'),
        ('repair', 'Repair'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_on = models.DateTimeField(auto_now_add=True)
    resolved_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.customer.username} - {self.request_type}"