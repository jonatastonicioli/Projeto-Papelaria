from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.CharField(max_length=255)
    ativa = models.BooleanField(default=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    codigo = models.CharField(max_length=10, unique =True)
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null = True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="produtos")

    def __str__(self):
        return self.nome