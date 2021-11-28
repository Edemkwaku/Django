from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse


# Create your models here.

class Bank(models.Model):
    code=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=50,unique=True)
    city=models.CharField(max_length=50)
    street=models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bank_details',kwargs={'pk':self.code})

class Branch(models.Model):
    bankcode=models.ForeignKey(Bank,on_delete=CASCADE)
    code=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    date_created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    customer=models.CharField(max_length=20,primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    town =models.CharField(max_length=50)
    house_no=models.CharField(max_length=50)
    date_created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name +', '+ self.last_name


class Account(models.Model):
    branchcode=models.ForeignKey(Branch,on_delete=CASCADE)
    customer=models.ForeignKey(Customer,on_delete=CASCADE)
    accountNunber=models.CharField(max_length=20,primary_key=True)
    type=models.CharField(max_length=50,null=False)
    Balance=models.DecimalField(max_digits=10, decimal_places=2,default=5)
    street=models.CharField(max_length=50,null=False)
    date_created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.account_no

class Loan(models.Model):
    branchcode=models.ForeignKey(Branch,on_delete=CASCADE)
    customer=models.ForeignKey(Customer,on_delete=CASCADE)
    loanId=models.CharField(max_length=20,primary_key=True)
    type=models.CharField(max_length=50)
    Amount=models.DecimalField(max_digits=10,decimal_places=2,default=5.00)

    def __str__(self):
        return self.loan_id,self.customer_id
