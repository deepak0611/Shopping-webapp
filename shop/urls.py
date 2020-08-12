
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="shophome"),
    path('about/',views.about,name="AboutUs"),
    path('contact/',views.contact,name="ContactUs"),
    path('tracker/',views.tracker,name="TrackingStatus"),
    path('search/',views.search,name="Search"),
    path('productview/',views.prodView,name="ProducView"),
    path('checkout/',views.checkout,name="Checkout"),
    path('add_item/',views.add_item,name="AddItem"),
]