from django.db import models

# Create your models here.

class Categoria(models.Model): 
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome
    