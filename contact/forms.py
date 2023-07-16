# flake8: noqa
from django import forms
from . import models
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )

    class Meta:
        model = models.Contact
        fields = (
            'first_name','last_name', 'phone', 'email','category',
            'description', 'picture',
            
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'classe-a classe-b','placeholder': 'Digite o primeiro nome.'
                    }
                ), 
            'last_name': forms.TextInput(
                attrs={
                    'placeholder':'Digite o sobrenome.'
                    }
                ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder':'Digite o e-mail do seu contato.'
                    }
                ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder':'Digite o número do seu contato.'
                    }
                ),
            'description': forms.Textarea(
                attrs={
                    'placeholder':'Faça uma descrição do seu contato.'
                    }
                ),
            }
        
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=5
    )
    last_name = forms.CharField(
        required=True,
        min_length=5
    )
    email = forms.EmailField(
        required=True,
        min_length=10
    )
    
    
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1',
            'password2',
        )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Este e-mail já existe.', code='invalid')
            )
