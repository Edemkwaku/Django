from django.urls import path
from bankSystem.views import BankList,BankDetail,BankCreate,BankUpdate,BankDelete,Branchs,BranchDelete, BranchUpdate
from bankSystem.views import Branch,BranchCreate,Customers,Customer,CustomerUpdate,CustomerDelete,CustomerCreate



urlpatterns = [
    #urls for bank views

    path('',BankList.as_view(),name='banks'),
    path('bank/<slug:pk>/',BankDetail.as_view(), name='bank_details'),
    path('create/',BankCreate.as_view(), name='bank_create'),
    path('bank/<slug:pk>/update/',BankUpdate.as_view(), name='bank_update'),
    path('bank/<slug:pk>/delete/',BankDelete.as_view(),name='bank_delete'),

    #urls for branch views
    path('banks/branchs/',Branchs.as_view,name='bank_branchs'),
    path('banks/branch/<slug:pk>/',Branch.as_view,name='branch_details'),
    path('banks/branchs/create/',BranchCreate.as_view,name='branch_create'),
    path('banks/branchs/<slug:pk>/update',BranchUpdate.as_view,name='branch_update'),
    path('banks/branchs/<slug:pk>/delete',BranchDelete.as_view,name='branch_delete'),

    #urls for customer Views
    path('banks/branchs/customers/',Customers.as_view(),name='customers'),
    path('banks/branchs/customer/<slug:pk>/',Customer.as_view(),name='customer_details'),
    path('banks/branchs/customers/<slug:pk>/update',CustomerUpdate.as_view(),name='update_customer'),
    path('banks/branchs/customers/create',CustomerCreate.as_view(),name='create_customer'),
    path('banks/branchs/customers/<slug:pk>/delete',CustomerDelete.as_view(),name='delete_customers'),
    
]