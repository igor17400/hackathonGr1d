from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=60)
    cpf = models.CharField(max_length=60)

    def __str__(self):
        return "name: {} || CPF: {}".format(self.name, self.cpf)
    
class Bank(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Operation(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    
class Account(models.Model):
    creation_date = models.DateField()
    balance = models.FloatField()
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.client.name

class Transaction(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return  "Operation: {} || Amount: {}".format(self.operation, self.amount)