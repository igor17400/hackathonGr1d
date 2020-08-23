from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
import requests

from .serializers import BankSerializer, ClientSerializer, AccountSerializer, TransactionSerializer, OperationSerializer
from .models import Bank, Client, Account, Transaction, Operation

def meuScore(request):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=fd38d62aa4fe1a03d86eee91fcd69f6e')
    url = 'https://gateway.gr1d.io/production/proScore/score/v1/?tcpfcnpj=06589184194&tdatnsc=10091997'
    r = requests.get(url, headers={'Authorization':'Bearer %s' % 'access_token'})
    response = requests.get('HTTPS://gateway.gr1d.io/production/proScore/score/v1/MeuScore/?X-Api-Key=8a66fd8e-b511-446a-b900-d3226fe48d4d')
    meuScore = response.json()
    return render(request, 'core/home.html', {
        'numero_plugin': meuScore['numero_plugin']
    })

class ClientViewSet(APIView):
    def get(self, request, *args, **kwargs):
        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data) 
        
class BankViewSet(APIView):
    def get(self, request, *args, **kwargs):
        bank = Bank.objects.all()
        serializer = BankSerializer(bank, many=True)
        return Response(serializer.data)


class AccountViewSet(APIView):
    def get(self, request, *args, **kwargs):
        account = Account.objects.all()
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)

class TransactionViewSet(APIView):
    def get(self, request, *args, **kwargs):
        transaction = Transaction.objects.all()
        serializer = TransactionSerializer(transaction, many=True)
        return Response(serializer.data)


class TransactionPerId(APIView):
    def get(self, request, id):
        try:
            transaction = Transaction.objects.filter(account=id)
            serializer = TransactionSerializer(transaction, many=True)
        except transaction.DoesNotExist:
            pass
        return Response(serializer.data)

class OperationViewSet(APIView):
    def get(self, request, *args, **kwargs):
        operation = Operation.objects.all()
        serializer = OperationSerializer(transaction, many=True)
        return Response(serializer.data)