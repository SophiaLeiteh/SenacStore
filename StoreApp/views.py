from django.shortcuts import render
from StoreApp.models import Departamento, Produto
from StoreApp.forms import CadastroForm, ContatoForm
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

def produto_detalhe(request, id):
    produto = Produto.objects.get(id = id)
    produtos_relacionados = Produto.objects.filter(departamento_id = produto.departamento).exclude(id = id)[:4]

    context = {
        'produto' : produto,
        'produtos_relacionados' : produtos_relacionados
    }
    return render(request, 'produto_detalhes.html', context)

def sobre_empresa(request):
    return render(request, 'sobre_empresa.html')

def cadastro(request):
    #armazenar msg de sucesso ou erro
    mensagem = ''
    #se o formulario foi submetido
    if request.method == 'POST':
        formulario = CadastroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            formulario = CadastroForm()
            mensagem = "Cliente cadastrado com sucesso."
        else:
            mensagem = "Verifique os erros abaixo: "

    #se o formulario não foi submetido. Entrei na pag. pelo menu
    #e o form deve vir vazio
    else:
        formulario = CadastroForm()

    context = {
        'formulario_cadastro' : formulario,
        'mensagem' : mensagem 
    }
    return render(request, 'cadastro.html', context)

def contato(request):
    mensagem = ''
    formulario = ContatoForm()


    context = {
        'mensagem': mensagem,
        'formulario_contato' : formulario

    }
    return render(request, 'contato.html', context)