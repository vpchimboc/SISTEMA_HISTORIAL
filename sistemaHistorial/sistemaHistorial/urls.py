"""
URL configuration for sistemaHistorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.login import LoginView, LogoutRedirectView
from app.views import *

urlpatterns = [
    #1
   path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutRedirectView.as_view(), name="logout"),
#2
    path('home', HomeView.as_view(), name='home'),
#3
    path('home/pacientes', PacienteListView.as_view(), name='paciente_list'),
    path('home/pacientes/create', PacienteCreateView.as_view(), name='paciente_create'),
    path('home/pacientes/edit/<slug:slug>', PacienteEditView.as_view(), name='paciente_edit'),
#4
    path('home/ficha_medica', FichaMedicaListView.as_view(), name='ficha_medica_list'),
    path('home/ficha_medica/create', FichaMedicaCreateView.as_view(), name='ficha_medica_create'),
    path('home/ficha_medica/edit/<int:pk>', FichaMedicaEditView.as_view(), name='ficha_medica_edit'),
#5
    path('home/consultas', ConsultaListView.as_view(), name='consulta_list'),
    path('home/consultas/create', ConsultaCreateView.as_view(), name='consulta_create'),
    path('home/consultas/edit/<int:pk>', ConsultaEditView.as_view(), name='consulta_edit'),

]
