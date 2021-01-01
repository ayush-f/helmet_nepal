from django import forms
from helmet.models import Helmet
class HelmetForm(forms.ModelForm):
        class Meta:
               model=Helmet
               fields="__all__"
