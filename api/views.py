from django.shortcuts import render
from .models import Categoria, Produto
from rest_framework.decorators import api_view
from .serializer import CategoriaSerializer
from .serializer import ProdutoSerializer
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET','POST'])
def listar_categorias(request): # nao tem o self pois o a funcao nao esta dentro de uma classe
    if request.method == 'GET':
        queryset = Categoria.objects.all() # SELECT * FROM categoria;
        serializers = CategoriaSerializer(queryset, many=True) #many true para pegar mais de um 

        return Response(serializers.data)

    elif request.method == 'POST':
        serializers = CategoriaSerializer(data=request.data) #salva o post do usuario na variavel serilalizer tudo em JSON
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','POST'])
def listar_produtos(request):
    if request.method == 'GET':
        queryset = Produto.objects.all()
        serializers = ProdutoSerializer(queryset, many=True)
        
        return Response(serializers.data)

    elif request.method == 'POST':
        serializers = ProdutoSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH'])
def detalhe_produto(request, pk):
    ...

    











        




# Create your views here.k
