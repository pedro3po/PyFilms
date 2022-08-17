from django.shortcuts import render, HttpResponse,redirect
from .models import Filmes
from .forms import FilmesForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')

@login_required
def detalhe(request, id_filme):
    filme = {'filmes':Filmes.objects.get(pk=id_filme)}
    return render(request,'filmes/detalhes.html', filme)

@login_required
def listar_filmes(request):
    filmes = {'filmes':Filmes.objects.all()}
    return render(request,'filmes/filmes.html',context=filmes)
    
@login_required
def novo_filme(request):
    if request.method == 'POST':
        filmes_form = FilmesForm(request.POST)
        if filmes_form.is_valid():
            filmes_form.save()
            return redirect('listar_filmes')
    else:
        filmes_form = FilmesForm()
        filmes = {'filmes': filmes_form}
        return render(request,'filmes/novo_filme.html', context=filmes)
        redirect('listar_filmes')

@login_required
def editar_filme(request, id_filme):
    filme = Filmes.objects.get(pk=id_filme)
    if request.method == 'GET':
        filmes = FilmesForm(instance=filme)
        return render(request,'filmes/novo_filme.html',{'filmes': filmes})
    else:
        formulario = FilmesForm(request.POST, instance=filme)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_filmes')

@login_required
def excluir_filmes(request, id_filme):
    filme = Filmes.objects.get(pk=id_filme)
    if request.method == 'POST':
        filme.delete()
        return redirect('listar_filmes')
    return render(request,'filmes/exclusao.html', {'item': filme})


