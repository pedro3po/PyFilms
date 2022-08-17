from django.urls import path
from accounts import views

urlpatterns = [
    path('register/',views.SignUp.as_view(),name='signup')
]