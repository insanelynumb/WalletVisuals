from django.urls import path
from expenses import views
app_name = 'expenses'
urlpatterns = [
    path('expense/', views.index, name='expense'),
    path('add_expense/', views.add_expense, name='add_expenses'),
    path('edit_expense/<int:id>', views.expense_edit, name='edit_expenses'),
    path('delete_expense/<int:id>', views.delete_expense, name='delete_expenses'),
    path('expense_category_summary/', views.expense_category_summary, name='expense_category_summary'),
    path('stats/', views.stats_view, name='stats'),
]
