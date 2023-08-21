from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from datetime import datetime
from django.contrib.sessions.models import Session
from django.contrib.auth.hashers import make_password,check_password
from .models import Customers,Transactions,CustomerSignIn,ATM
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def index(request):
    return render(request,'index.html')

def admin(request):
    customer_data = Customers.objects.all()
    context = {
        'Customers':customer_data
    }
    return render(request,'admin_template/admin.html',context)

def insert(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        amount = request.POST.get('amount')
        account_id = request.POST.get('account_id')
        customercpr =  request.POST.get('customercpr')
        pincode = request.POST.get('pincode')
        password =  request.POST.get('password')
        
        # Check if the email already exists in the database
        if Customers.objects.filter(email=email).exists():
            error_message = "Customer Exists Already"
            return render(request, 'admin_template/insert.html', {'error_message': error_message})
        
        # Create a new customer if the email doesn't exist
        new_customer = Customers(name=name, email=email, amount=amount, account_id=account_id,customer_cpr=customercpr,pin_code=pincode,password=password)
        new_customer.save()
        return redirect('/admin_panel/')  # Redirect to a suitable page after successful insertion
        
    return render(request, 'admin_template/insert.html')
    
def edit(request, pk):

    customer = Customers.objects.get(pk=pk)  # Assuming Customers is the model representing your customer data

    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        amount = request.POST.get('amount')
        account_id = request.POST.get('account_id')
        customercpr = request.POST.get('customercpr')
        pincode = request.POST.get('pincode')
        password =  request.POST.get('password')


        customer = Customers.objects.get(pk=pk)  # Assuming Customers is the model representing your customer data

        # Update the customer's information
        customer.name = name
        customer.email = email
        customer.amount = amount
        customer.account_id = account_id
        customer.customer_cpr = customercpr
        customer.pin_code = pincode
        customer.password = password
        customer.save()
        
        return redirect('admin_panel')  # Redirect to a suitable page after successful update
        
    return render(request, 'admin_template/edit.html', {'customer': customer})

def delete(request, pk):
    customer = Customers.objects.get(pk=pk)
    customer.delete()
    return redirect('/admin_panel/') 

def account_verifiction(request):
    if request.method == 'POST':
        accountNo = request.POST.get('account_no')
        pincode = request.POST.get('pincode')
        password = request.POST.get('password')

        try:
            customer = Customers.objects.get(account_id=accountNo)

            # Assuming 'pincode' and 'password' are attributes in the 'Customers' model
            if customer.pin_code == pincode and customer.password == password:
                # Password and pincode match, proceed with the verification

                atm_data = ATM.objects.all()

                context = {
                    'user_data': customer,
                    'atm_data': atm_data
                }
                return render(request, 'profile.html', context)
            else:
                # Password and/or pincode do not match
                context = {
                    'error_message': 'Invalid pincode and/or password'
                }
                return render(request, 'account_verifi.html', context)

        except ObjectDoesNotExist:
            context = {
                'error_message': 'Account not found. Please contact the administrator.'
            }
            return render(request, 'account_verifi.html', context)

    return render(request, 'account_verifi.html')
def transaction_form(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        amount = request.POST.get('amount')
        location = request.POST.get('account_type')    
    
        if customer_id and amount and location:  
            try:
                customer = Customers.objects.get(id=customer_id)
                new_amount = float(customer.amount) - float(amount)

                if new_amount >= 0:
                    customer.amount = new_amount
                    customer.save()

                    atm_instance, created = ATM.objects.get_or_create(ATM_location=location)


                    transaction = Transactions.objects.create(
                        transaction_date=datetime.now(),
                        transaction_amount=float(amount),
                        transaction_status="Completed",
                        customer=customer,
                        atm=atm_instance
                        
                    )


                    

                    context = {
                        'user_data': customer,
                        
                    }


                    return render(request, 'profile.html', context)
                else:
                    error_message = "Insufficient funds."
            except Customers.DoesNotExist:
                error_message = "Customer not found."
        else:
            error_message = "Invalid data."
        
        context = {
            'error_message': error_message
        }
        return render(request, 'profile.html', context)  # Create an error template
    
    
    
    return render(request, 'profile.html',context)

def transaction_details(request):
    transaction_data = Transactions.objects.all()
    context = {
        'transactions':transaction_data
    }
    return render(request,'admin_template/transactions.html',context)

def admin_signin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')



        customer_email = CustomerSignIn.objects.filter(email=email)
        print(customer_email)
        if customer_email:
            return redirect('/admin_panel/')
        else:
            context = {
                'error_message':"Incorrect Admin credentials"
            }

            return render(request,'sigin.html',context)
    return render(request,'sigin.html')
