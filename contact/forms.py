from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from contact.models import Contact

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'aqui eh do outro',
            }
        ),
        # label='PRIMEIRO NOME'
        help_text='texto de ajuda para seu user'
    )

    # Modificar widgets
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['first_name'].widget.attrs.update({
    #             'class': 'classe-a classe-b',
    #             'placeholder': 'VEIO DO INIT',
    #     })

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
        )

        # criar widget
        # widgets = {
        #     'first_name': forms.TextInput(attrs={
        #         'class': 'classe-a classe-b',
        #         'placeholder': 'escreva aqui',
        #     })
        # }
        
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome nao esta pode ser igual ao segundo',
                code='invalid'
            )
            self.add_error(
                'first_name', msg)
            self.add_error(
                'last_name', msg)



    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError('VEIO DO ADD ERROR',
                                code='invalid'
                )
            )
            
        return first_name
    # Erro com Raise (desvantagem: para o codigo no erro)
    # def clean_first_name(self):
    #     first_name = self.cleaned_data.get('first_name')
    #     if first_name == 'ABC':
    #         raise ValidationError(
    #             'Nao digite ABC neste campo',
    #             code='invalid'
    #             )

        print('Passei no clean do first_name')
        return first_name