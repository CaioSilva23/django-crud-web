from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm


# Create your views here.

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


def inserir_cliente(request):
    if request.method == "POST":
        # instancia do formulario recebendo os dados da requisição
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')  # REDIRECIONA PARA A LISTAGEM
    else:
        form = ClienteForm()
    return render(request, 'clientes/form_cliente.html', {'form': form})


def listar_cliente_id(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, 'clientes/listar_cliente_id.html', {'cliente': cliente})


def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('listar_clientes')
    return render(request, 'clientes/form_cliente.html', {'form': form})


def remover_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'clientes/confirma_exclusao.html', {'cliente': cliente})
