from django.shortcuts import render, redirect
from authentication.forms import UserRegistrationForm
from django.http import JsonResponse
from datetime import date, timedelta
from user_income.models import UserIncome
from expenses.models import Expense
def signup(request):
    if request.user.is_authenticated:
        return redirect('authentication:home')
    else:
        if request.method == "POST":
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserRegistrationForm()

        context = {
            'title': 'Sign Up',
            'form': form
        }
        return render(request, 'signup.html', context)

def home(request):
    todays_date = date.today()
    first_day_of_month = todays_date.replace(day=1)

    incomes = UserIncome.objects.filter(
        owner=request.user,
        date__gte=first_day_of_month,
        date__lte=todays_date
    )

    total_income = sum(income.amount for income in incomes)

    expenses = Expense.objects.filter(
        owner=request.user,
        date__gte=first_day_of_month,
        date__lte=todays_date
    )

    total_expenses = sum(expense.amount for expense in expenses)

    return render(request, 'home.html', {'total_income': total_income, 'total_expenses': total_expenses})

def expense_category_summary(request):
    todays_date = date.today()
    first_day_of_month = todays_date.replace(day=1)

    expenses = Expense.objects.filter(
        owner=request.user,
        date__gte=first_day_of_month,
        date__lte=todays_date
    )

    expense_category_summary = {}

    def get_category(expense):
        return expense.category

    category_list = list(set(map(get_category, expenses)))

    def get_expense_category_amount(category):
        amount = 0
        filtered_by_category = expenses.filter(category=category)

        for item in filtered_by_category:
            amount += item.amount
        return amount

    for y in category_list:
        expense_category_summary[y] = get_expense_category_amount(y)

    return JsonResponse({'expense_category_data': expense_category_summary}, safe=False)


def income_category_summary(request):
    todays_date = date.today()
    first_day_of_month = todays_date.replace(day=1)

    incomes = UserIncome.objects.filter(
        owner=request.user,
        date__gte=first_day_of_month,
        date__lte=todays_date
    )

    income_category_summary = {}

    def get_category(income):
        return income.source  # Assuming 'source' is the category field in UserIncome

    category_list = list(set(map(get_category, incomes)))

    def get_income_category_amount(category):
        amount = 0
        filtered_by_category = incomes.filter(source=category)  # Change 'category' to 'source'

        for item in filtered_by_category:
            amount += item.amount
        return amount

    for category in category_list:
        income_category_summary[category] = get_income_category_amount(category)

    return JsonResponse({'income_category_data': income_category_summary}, safe=False)
