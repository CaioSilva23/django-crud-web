from django import forms

from clientes.models import Cliente


class ClienteForms(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sexo', 'data_nascimento', 'email', 'profissao']
