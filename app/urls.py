from django.urls import path
from .import views
urlpatterns = [

    path('',views.index,name="index"),
    path('admin_panel/',views.admin,name="admin_panel"),
    path('admin_panel/insert/',views.insert,name="insert_page"),
    path('admin_panel/edit/<int:pk>/',views.edit,name="edit_page"),
    path('admin_panel/delete/<int:pk>/',views.delete,name="delete_function"),
    path('account_verifiction/',views.account_verifiction,name="account_verification"),
    path('transactionform/',views.transaction_form,name="transaction_form"),
    path('transaction_details/',views.transaction_details,name="transaction_details"),
    path('admin_signin/',views.admin_signin,name="admin_signup")
   
]


