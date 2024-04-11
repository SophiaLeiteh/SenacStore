from django.shortcuts import render
from StoreApp.models import Departamento, Produto
# Create your views here.
def index(request):
    produtos_destaque = Produto.objects.filter(destaque = True)


    context = {
        'produtos' : produtos_destaque
    }
    return render(request, 'index.html', context)


def produtos_lista(request):
    produtos_lista = Produto.objects.all()

    context = {
        'produtos' : produtos_lista,
        'titulo' : 'Produtos'
    }

    return render(request, 'produtos.html', context)

def produto_detalhe(request, id):
    produto = Produto.objects.get(id=id)
    
    context = {
        'produto' : produto
    }
    return render(request, 'produto_detalhes.html', context)

def produtos_lista_por_departamento(request, id):
    produtos_lista = Produto.objects.filter(departamento_id = id)
    departamento = Departamento.objects.get(id = id)

    context = {
        'produtos' : produtos_lista,
        'titulo' : departamento.nome
    }

    return render(request, 'produtos.html', context)