from django.contrib import admin
from expenses.models import Category, Expense

admin.site.register(Expense)
admin.site.register(Category)