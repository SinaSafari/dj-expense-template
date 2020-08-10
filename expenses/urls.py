from django.urls import path
from expenses.views import index, add_expense

urlpatterns = [
    path('', index, name='expense_index'),
    path('add-expense', add_expense, name='add_expense')
]