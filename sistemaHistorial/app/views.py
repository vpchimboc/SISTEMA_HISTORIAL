from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import TemplateView, ListView, CreateView, UpdateView

from app.forms import PacienteForm, FichaMedicaForm, ConsultaForm
from app.models import Paciente, Ficha_Medica, Consulta


# Create your views here.
####1
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paciente'] = Paciente.objects.all().count()
        context['ficha_medica'] = Ficha_Medica.objects.all().count()
        context['consulta'] = Consulta.objects.all().count()
        return context
    
########2
class PacienteListView(LoginRequiredMixin, ListView):
    template_name = 'paciente/list.html'
    model = Paciente
    context_object_name = 'paciente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_list'] = 'Listado de Pacientes'
        return context


class PacienteCreateView(LoginRequiredMixin, CreateView):
    template_name = 'paciente/form.html'
    model = Paciente
    form_class = PacienteForm
    success_url = reverse_lazy('paciente_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = 'Nuevo Paciente'
        return context


class PacienteEditView(LoginRequiredMixin, UpdateView):
    template_name = 'paciente/form.html'
    model = Paciente
    form_class = PacienteForm
    success_url = reverse_lazy('paciente_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = 'Editar Paciente'
        return context
#############3
class FichaMedicaListView(LoginRequiredMixin, ListView):
    template_name = 'ficha_medica/list.html'
    model = Ficha_Medica
    context_object_name = 'ficha_medica'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_list'] = 'Listado de Fichas Médicas'
        return context


class FichaMedicaCreateView(LoginRequiredMixin, CreateView):
    template_name = 'ficha_medica/form.html'
    model = Ficha_Medica
    form_class = FichaMedicaForm
    success_url = reverse_lazy('ficha_medica_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = 'Nueva Ficha Médica'
        return context


class FichaMedicaEditView(LoginRequiredMixin, UpdateView):
    template_name = 'ficha_medica/form.html'
    model = Ficha_Medica
    form_class = FichaMedicaForm
    success_url = reverse_lazy('ficha_medica_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = 'Editar Ficha Médica'
        return context

#############4
class ConsultaListView(LoginRequiredMixin, ListView):
    template_name = 'consulta/list.html'
    model = Consulta
    context_object_name = 'consulta'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_list'] = 'Listado de Consultas'
        return context


class ConsultaCreateView(LoginRequiredMixin, CreateView):
    template_name = 'consulta/form.html'
    model = Consulta
    form_class = ConsultaForm
    success_url = reverse_lazy('consulta_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = 'Nueva Consulta'
        return context


class ConsultaEditView(LoginRequiredMixin, UpdateView):
    template_name = 'consulta/form.html'
    model = Consulta
    form_class = ConsultaForm
    success_url = reverse_lazy('consulta_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = 'Editar Consulta'
        return context