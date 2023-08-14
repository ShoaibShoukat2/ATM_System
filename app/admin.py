from django.contrib import admin
from .models import Customers,Transactions,CustomerSignIn,ATM
# register models


class CustomerTable(admin.ModelAdmin):
    list_display = ('id','name','email','amount','account_id')

admin.site.register(Customers,CustomerTable)

class TransactionTable(admin.ModelAdmin):
    list_display = ('id','transaction_date','transaction_amount','transaction_status','customer','atm','completed')

admin.site.register(Transactions,TransactionTable)


class adminTable(admin.ModelAdmin):
    list_display = ('id','name','email')

admin.site.register(CustomerSignIn,adminTable)

class AtmTable(admin.ModelAdmin):
    list_display = ('id','ATM_location')
admin.site.register(ATM,AtmTable)
