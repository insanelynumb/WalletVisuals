from django.urls import path
from authentication import views
app_name = 'authentication'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('expense_category_summary/', views.expense_category_summary, name='expense_category_summary'),
    path('income_category_summary/', views.income_category_summary, name='income_category_summary'),
]
