
from rest_framework.authtoken import views
from .views import RegisterView
from django.urls import path

urlpatterns = [
   
    path("register/",RegisterView.as_view() ),
    path("login/",views.obtain_auth_token ),
]
