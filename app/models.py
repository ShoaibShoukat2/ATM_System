from django.db import models




class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100,default='')
    name = models.CharField(max_length=100,default='')
    amount = models.IntegerField(default=0)
    account_id = models.IntegerField(default=0)


    def __str__(self):
        return self.name
    


class ATM(models.Model):
    id = models.AutoField(primary_key=True)
    LOCATION_CHOICES = [
        ('Alexander City', 'Alexander City'),
        ('Andalusia', 'Andalusia'),
        ('Anniston', 'Anniston'),
        ('Athens', 'Athens'),
        ('Atmore', 'Atmore'),
        # Add more choices as needed

    ]
    ATM_location = models.CharField(max_length=200,choices=LOCATION_CHOICES,default='location')


    def __str__(self):
        return self.ATM_location
            
    
class Transactions(models.Model):
    id = models.AutoField(primary_key=True)
    transaction_date = models.DateTimeField()
    transaction_amount = models.FloatField()
    transaction_status = models.CharField(max_length=50)  # You can adjust the max_length as needed
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    atm = models.ForeignKey(ATM,on_delete=models.CASCADE)
    # atm = models.ForeignKey(ATM,on_delete=models.CASCADE)
    completed = models.BooleanField(default=True)

    def __str__(self):
        return f"Transaction {self.id} for {self.customer.name}" 
    

class CustomerSignIn(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')


    def __str__(self):
        return self.name