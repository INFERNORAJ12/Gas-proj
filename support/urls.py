from django.urls import path
from . import views

urlpatterns = [
    path('support/', views.request_list, name='support_list'),
    path('support/update/<int:request_id>/', views.update_request, name='update_request'),
]