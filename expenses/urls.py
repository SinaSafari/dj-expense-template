from django.urls import path
from expenses.views import index, add_expense, expense_edit, delete_expense, search_expenses
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', index, name='expenses'),
    path('add-expense', add_expense, name='add-expense'),
    path('edit-expense/<int:id>', expense_edit, name="expense-edit"),
    path('expense-delete/<int:id>', delete_expense, name="expense-delete"),
    path('search-expenses', csrf_exempt(search_expenses), name="search_expenses"),
]