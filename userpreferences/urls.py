from django.urls import path
from userpreferences.views import index

urlpatterns = [
    path('', index, name="preferences")
]