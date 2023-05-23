from django.forms import ModelForm

from app.models import Paciente, Ficha_Medica, Consulta


class PacienteForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Paciente
        fields = '__all__'
        exclude = ['fecha_registro']


class FichaMedicaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Ficha_Medica
        fields = '__all__'
        exclude = ['fecha_registro']


class ConsultaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Consulta
        fields = '__all__'
        exclude = ['fecha_registro']