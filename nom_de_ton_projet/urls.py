from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('predict/', views.predict_diabetes, name='predict'),
    path('', views.predict_diabetes, name='home'),  # Définition de la page d'accueil
]
