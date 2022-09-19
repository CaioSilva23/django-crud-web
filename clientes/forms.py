from django import forms

from clientes.models import Cliente


class ClienteForms(forms.ModelForm):
    # nome = forms.CharField(widget=forms.Textarea())  # ALTERANDO O TAMANHO DA CAIXA DE TEXTO

    class Meta:
        model = Cliente
        fields = ['nome', 'sexo', 'data_nascimento', 'email', 'profissao']
