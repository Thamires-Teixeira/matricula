
from django.shortcuts import render,get_object_or_404,redirect
from aluno.models import Aluno,Curso,Cidade
from .forms import CursoForm

def curso_editar(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        print("CHEGOU AQUI")
        if form.is_valid():
            print("CHEGOU AQUI 2 ")

            form.save()
            return redirect('curso_listar')
    else:
        form =  CursoForm(instance=curso)
    return render(request, 'curso/form.html', {'form': form})



def curso_remover(request, id):
    curso = get_object_or_404(Curso, id=id)
    curso.delete()
    return redirect('curso_listar') # procure um url com o nome 'lista_aluno'


def curso_criar(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            form = CursoForm()
    else:
        form = CursoForm()

    return render(request, "curso/form.html", {'form': form})


def curso_listar(request):
    cursos = Curso.objects.all()
    context ={
        'cursos':cursos
    }
    return render(request, "curso/cursos.html",context)


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