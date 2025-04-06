from django import forms
from .models import Processo
from .models import Compromisso

class ProcessoForm(forms.ModelForm):
    class Meta:
        model = Processo
        fields = ['cliente', 'numero', 'descricao', 'status', 'data_abertura']
        
class CompromissoForm(forms.ModelForm):
    class Meta:
        model = Compromisso
        fields = ['cliente', 'processo', 'titulo', 'data', 'local', 'descricao']
        widgets = {
            'data': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
