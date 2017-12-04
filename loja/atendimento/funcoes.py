from django.shortcuts import render
from django.http import HttpResponse
from atendimento.models import *

def resultado(request):
    retorno = "<h1> RESULTADO DAS VENDAS </h1> <br>"
    listaVenda = Vendas.objects.all()
    for e in listaVenda:
        retorno+=  " <h2> &emsp;VENDEDOR: {} </ h2> <br> <br>" .format(e.vendendor)
        retorno+=  " <h2> &emsp;PRODUTO: {} </ h2> <br> <br>" .format(e.produto)
        retorno+=  " <h2> &emsp;PRODUTO: {} </ h2> <br> <br>" .format(e.valor)
        retorno+=  " <h2> &emsp;PRODUTO: {} </ h2> <br> <br>" .format (e.quantidade)
        retorno+=  " <h2> &emsp;VENDEDOR: {} </ h2> <br> <br>" .format(e.vendendor)
        retorno+=  " <h2> &emsp;PRODUTO: {} </ h2> <br> <br>" .format(e.produto)
        valor= (int(e.valor))
        valordois=(int(e.quantidade))
        retorno+=  " <h2> &emsp;Resultado: {} </ h2> <br> <br>" .format (valor*valordois)
    return HttpResponse(retorno)
def resultado2(request):
    retorno = "<h1> RESULTADO DAS VENDAS </h1> <br>"
    cliente = Cliente.objects.all()
    for e in cliente:
        retorno+=  " <h2> &emsp;VENDEDOR: {} </ h2> <br> <br>" .format(e.nome)
        retorno+=  " <h2> &emsp;VENDEDOR: {} </ h2> <br> <br>" .format(e.cpf)
    return HttpResponse(retorno)
def resultado3(request):
    retorno = "<h1> RESULTADO DAS VENDAS </h1> <br>"
    retorno+=  " <h2> &emsp;VENDEDOR: {} </ h2> <br> <br>" (Vendas.objects.filter(vendendor="David Xavier"))
    return HttpResponse(retorno)
