from django.forms import ModelForm
from .models import Filmes

class FilmesForm(ModelForm):
    class Meta:
        model = Filmes
        fields = '__all__'