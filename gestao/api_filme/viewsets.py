from rest_framework import viewsets
from gestao.api_filme import serializers
from gestao import models

class FilmesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FilmesSerializer
    queryset = models.Filmes.objects.all()
