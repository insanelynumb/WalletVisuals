from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from user_income import views
app_name = 'user_income'
urlpatterns = [
    path('income_home/', views.index, name='home'),
    path('add_income/', views.add_income, name='add_income'),
    path('edit_income/<int:id>', views.income_edit, name='edit_income'),
    path('delete_income/<int:id>', views.delete_income, name='delete_income'),
    path('search_income/', csrf_exempt(views.search_income), name="search_income"),
    path('income_category_summary/', views.income_category_summary, name='income_category_summary'),
    path('income_stats/', views.stats_view, name='income_stats'),
]
