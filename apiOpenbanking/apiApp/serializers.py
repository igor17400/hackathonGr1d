from rest_framework import serializers

from .models import Bank, Client, Account, Transaction, Operation

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('id', 'name')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'cpf')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'creation_date', 'balance', 'creation_date', 'bank')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('operation', 'account', 'amount', 'date')

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ('name')