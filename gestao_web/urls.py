"""gestao_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from gestao.api_filme import viewsets as filmesviewset
from gestao import views


route = routers.DefaultRouter()
route.register(r'filmes',filmesviewset.FilmesViewSet, basename='Filmes')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/',include(route.urls)),
    path('', views.index, name='index'),
    path('novo_filme/', views.novo_filme, name='novo_filme'),
    path('novo_filme/<int:id_filme>', views.editar_filme, name='editar'),
    path('<int:id_filme>', views.detalhe, name='detalhe'),
    path('exclusao/<int:id_filme>', views.excluir_filmes, name='exclusao'),
    path('filmes/', views.listar_filmes, name='listar_filmes'),
]