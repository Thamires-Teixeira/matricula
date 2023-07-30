
from django.shortcuts import render,get_object_or_404,redirect
from aluno.models import Aluno,Curso,Cidade
from .forms import CidadeForm

def cidade_editar(request, id):
    cidade = get_object_or_404(Cidade, id=id)
    if request.method == 'POST':
        form = CidadeForm(request.POST, request.FILES, instance=cidade)
        print("CHEGOU AQUI")
        if form.is_valid():
            print("CHEGOU AQUI 2 ")

            form.save()
            return redirect('cidade_listar')
    else:
        form =  CidadeForm(instance=cidade)
    return render(request, 'cidade/form.html', {'form': form})



def cidade_remover(request, id):
    cidade = get_object_or_404(Cidade, id=id)
    cidade.delete()
    return redirect('cidade_listar') # procure um url com o nome 'lista_aluno'


def cidade_criar(request):
    if request.method == 'POST':
        form = CidadeForm(request.POST)
        if form.is_valid():
            form.save()
            form = CidadeForm()
    else:
        form = CidadeForm()

    return render(request, "cidade/form.html", {'form': form})


def cidade_listar(request):
    cidades = Cidade.objects.all()
    context ={
        'cidades':cidades
    }
    return render(request, "cidade/cidades.html",context)


def index(request):
    total_alunos = Aluno.objects.count()
    total_cidades = Cidade.objects.count()
    total_curso = Curso.objects.count()
    context = {
        'total_alunos' : total_alunos,
        'total_cidades' : total_cidades,
        'total_cursos' : total_curso
    }
    return render(request, "aluno/index.html",context)