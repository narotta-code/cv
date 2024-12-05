from django.urls import path
from . import views

urlpatterns = [
    path('account/home/', views.accountHome , name="home"),
]
