from rest_framework import viewsets  # viewsets para criar CRUD da API automaticamente
from .models import Pessoas  # modelo Pessoas do app
from .serializers import PessoasSerializer  # serializer para o modelo Pessoas

# ViewSet para o recurso Pessoas:
# - fornece endpoints padrão (list, retrieve, create, update, destroy) pelo ModelViewSet
class PessoasViewSet(viewsets.ModelViewSet):
    serializer_class = PessoasSerializer  # serializer usado para (de)serializar Pessoas

    def get_queryset(self):
        ordenacao = self.request.query_params.get('ordenar','id')

        campos_validos = ['id', '-id', 'cidade', '-cidade']

        if ordenacao not in campos_validos:
            ordenacao = 'id'


        return Pessoas.objects.all().order_by(ordenacao)    

