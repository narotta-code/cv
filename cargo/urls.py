from . import views
from django.urls import path
urlpatterns = [
    path('cargo/', views.cargo_View , name="cargo"),
]