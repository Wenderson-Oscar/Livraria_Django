from django.shortcuts import render, get_object_or_404
from livraria.models import Autor, Categoria, Livro
from django.contrib.auth import authenticate, login, logout


def logout_usuario(request):
    logout(request)
    return render(request, 'livraria/login.html',{})


def autenticar_usuario(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        livros = Livro.objects.all()
        return render(request, 'livraria/listar_livros.html', {'livros':livros})
    else:
        return render(request, 'livraria/login.html',{})


def page_login(request):
    return render(request, 'livraria/login.html',{})


def buscar_livro(request):
    infor = request.POST['infor']
    livros = Livro.objects.filter(nome__contains=infor)
    return render(request, 'livraria/listar_livros.html', {'livros':livros})


def detalhar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    return render(request, 'livraria/detalhar_livro.html', {'livro':livro})


def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'livraria/listar_categorias.html', {'categorias': categorias})


def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, 'livraria/listar_autores.html', {'autores': autores})


def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livraria/listar_livros.html',{'livros': livros})

