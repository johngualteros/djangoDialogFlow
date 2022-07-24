from django.urls import path
from . import views
urlpatterns = [
    path('',views.requests ,name="requests")
]
