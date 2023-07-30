from django.db import models
from curso.models import Curso
from cidade.models import Cidade
# Create your models here.


class Aluno(models.Model):
    imagem = models.ImageField(upload_to='static/image', null=True,blank=True)
    nome_aluno = models.CharField(max_length=150)
    endereco = models.CharField(max_length=250)
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE) 