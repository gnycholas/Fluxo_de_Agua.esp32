from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import datetime


def get_data_arduino(request):
    queryset_data = DataArduino.objects.order_by('-id')[:60]
    array_data = []
    for x in range(len(queryset_data)):
        array_data.append([x, queryset_data[x].vazao])

    consumo_mensal = round(sum([data.vazao for data in DataArduino.objects.filter(
        date__year=datetime.date.today().year, date__month=datetime.date.today().month)])/60, 2)

    consumo_diario = round(sum([data.vazao for data in DataArduino.objects.filter(
        date__year=datetime.date.today().year,
        date__month=datetime.date.today().month,
        date__day=datetime.date.today().day)])/60, 2)

    consumo_excessivo = {
        'mensagem': "Você ultrapassou a média de consumo díario por pessoa.",
        'status': "red"
    }
    consumo_normal = {
        'mensagem': "Seu consumo de Água está bom.",
        'status': "green"
    }

    if consumo_diario > 60:
        mensagem = consumo_excessivo
    else:
        mensagem = consumo_normal

    data = {
        'data': array_data,
        'consumo_mensal': consumo_mensal,
        'consumo_diario': consumo_diario,
        'mensagem': mensagem
    }
    return JsonResponse(data, safe=False)
