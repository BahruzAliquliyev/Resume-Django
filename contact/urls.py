from django.urls import path
from .views import contact_form, contact

urlpatterns = [

    path('contact_form', contact_form, name='contact'),
    path('contact', contact, name='contact'),
]
