from django.shortcuts import render
from .models import Categoria
from rest_framework.decorators import api_view
from .serializer import CategoriaSerializer
from rest_framework.response import Response

@api_view(['GET'])
def listar_categorias(request):
    if request.method == 'GET':
        queryset = Categoria.objects.all()
        serializers = CategoriaSerializer(queryset, many=True)

        return Response(serializers.data)


        




# Create your views here.k
