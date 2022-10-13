from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),
    path('listar_autores', views.listar_autores, name='listar_autores'),
    path('listar_categorias', views.listar_categorias, name='listar_categorias'),
    path('livro/<int:id>/', views.detalhar_livro, name='detalhar_livro'),
    path('buscar_livro', views.buscar_livro, name='buscar_livro'),
    path('page_login', views.page_login, name='page_login'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
    path('logout_usuario', views.logout_usuario, name='logout_usuario'),
]