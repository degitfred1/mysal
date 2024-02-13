from django.urls import path
from . import views

urlpatterns=[

   path('cool/',views.ban,name='cool') 
]