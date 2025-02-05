from tkinter import N
from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='Index'),
    path('mdetails/<moviename>',views.mdetails,name='Mdetails'),
    path('mdetails/seat/<moviename>',views.seat,name='Seat'),
    path('mdetails/seat/payment/<moviename>',views.payment,name='Payment'),
    path('mdetails/seat/payment/details/<moviename>',views.details,name='Details'),
    path('mdetails/seat/payment/details/print/<moviename>',views.print,name='Print'),
    path('login',views.login,name='login'),
    path('registration',views.registor,name='registor')
]