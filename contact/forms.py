
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder':'escribre tu nombre'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control','placeholder':'escribre tu email'}
    ),min_length=3,max_length=100)
    message = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class': 'form-control','rows':3,'placeholder':'escribre tu mensaje'}
    ),min_length=3,max_length=1000)