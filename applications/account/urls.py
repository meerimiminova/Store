from django.urls import path
from . import views

from applications.account.views import RegistrationView, LoginView, LogoutView, ProfileView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('profile-update/<int:pk>/', views.ProfileUpdateView.as_view())
]