from rest_framework.serializers import (
    ModelSerializer, 
    ValidationError,
    SerializerMethodField
)

from .models import Categoria
from .models import Produto

class CategoriaSerializer (ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProdutoSerializer (ModelSerializer):
    valor_total = SerializerMethodField()
    class Meta:
        model = Produto
        fields = '__all__'

    def get_valor_total(self, produto):
        total = produto.preco*produto.quantidade
        return format(total,":.2f")

    def validate_preco(self, valor):
        if valor < 0:
            raise ValidationError("O valor do produto deve ser maior que 0")
        return valor

    def validate_quantidade(self, valor):
        if valor < 0:
            raise ValidationError("A quantidade deve ser maior que zero")
        return valor
        


    