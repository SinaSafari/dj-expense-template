from django.urls import path
from userincome.views import index, add_income, income_edit, delete_income, search_income
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', index, name="income"),
    path('add-income', add_income, name="add-income"),
    path('edit-income/<int:id>', income_edit, name="income-edit"),
    path('income-delete/<int:id>', delete_income, name="income-delete"),
    path('search-income', csrf_exempt(search_income), name="search_income")
]