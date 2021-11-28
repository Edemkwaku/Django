from django.db.models import fields
from django.db.models.base import Model
from django.shortcuts import render
from django.urls.base import reverse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from bankSystem.models import Bank,Branch,Customer,Account,Loan


# Views for Bank
class BankList(ListView):
    model=Bank

class BankDetail(DetailView):
    model=Bank

    def get_absolute_url(self):
        return reverse('bank_details',kwargs={'pk':self.id})

class BankCreate(CreateView):
    model=Bank
    fields= "__all__"
    def get_absolute_url(self):
        return reverse('bank_details',kwargs={'pk':self.id})

class BankUpdate(UpdateView):
    model=Bank
    fields='__all__'

class BankDelete(DeleteView):
    model=Bank
    success_url=reverse_lazy('banks')
   
#Views for branch

class Branchs(ListView):
    model=Branch

    def get_absolute_url(self):
        return reverse('branch_details',kwargs={'pk':self.id})

class Branch(DetailView):
    model=Branch

    def get_absolute_url(self):
        return reverse('branch_details',kwargs={'pk':self.id})

class BranchCreate(CreateView):
    model=Branch
    fields='__all__'

    def get_absolute_url(self):
        return reverse('branch_details',kwargs={'pk':self.id})

class BranchUpdate(UpdateView):
    model=Branch
    fields='__all__'

class BranchDelete(DeleteView):
    model=Branch
    success_url='/bank_branchs/'


#Views for Customer

class Customers(ListView):
    model=Customer
    
class Customer(DetailView):
    model=Customer

    def get_absolute_url(self):
        return reverse('customer_details',kwargs={'pk':self.id})


class CustomerCreate(CreateView):
    model=Customer
    fields='__all__'

    def get_absolute_url(self):
        return reverse('customer_details',kwargs={'pk':self.id})

class CustomerUpdate(UpdateView):
    model=Customer
    fields='__all__'

class CustomerDelete(DeleteView):
    model=Customer
    success_url='/customers/'
    


# Create your views here.
