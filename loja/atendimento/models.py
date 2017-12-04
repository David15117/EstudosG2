# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=128)
    cpf= models.CharField(max_length=128)
    identidade=models.CharField(max_length=20)
    endere=models.CharField(max_length=128)
    telefone=models.CharField(max_length=128)
    def __str__(self):
        return '{}'.format(self.nome)
class Vendedor(models.Model):
    user = models.OneToOneField(User, null=True, blank=False)
    matricula= models.CharField(max_length=128)
    nome= models.CharField(max_length=128)
    endere= models.CharField(max_length=128)
    telefone= models.CharField(max_length=128)
    cpf= models.CharField(max_length=128)
    def __str__(self):
        return '{}'.format(self.nome)
class Produto(models.Model):
    codigo =models.CharField(max_length=128)
    descri=models.TextField(max_length=128)
    quantidade=models.IntegerField()
    def __str__(self):
        return '{}'.format(self.codigo)
class Vendas(models.Model):
    vendendor= models.ForeignKey(Vendedor, null=True, blank=False)
    produto=models.ForeignKey(Produto, null=True, blank=False)
    datatime=models.DateTimeField()
    valor =models.CharField(max_length=128)
    tipo =models.BooleanField("Avista",default=True)
    vencimento=models.DateField(null=True, blank=True)
    quantidade=models.IntegerField()
    def __str__(self):
        return '{}'.format(self.produto)