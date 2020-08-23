from django.contrib import admin
from .models import Bank, Client, Account, Transaction, Operation

admin.site.register(Bank)
admin.site.register(Client)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Operation)
