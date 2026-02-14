from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Expense
from django.db.models import Sum

def dashboard(request):
    expenses = Expense.objects.all()

    total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0

    category_data = Expense.objects.values('category').annotate(total=Sum('amount'))

    categories = [x['category'] for x in category_data]
    amounts = [x['total'] for x in category_data]

    return render(request, 'index.html', {
        'expenses': expenses,
        'total': total,
        'categories': categories,
        'amounts': amounts
    })

def add_expense(request):
    if request.method == "POST":
        Expense.objects.create(
            title=request.POST['title'],
            category=request.POST['category'],
            amount=request.POST['amount'],
            date=request.POST['date']
        )
        return redirect('/')
    return render(request, 'add.html')

def edit_expense(request, id):
    expense = Expense.objects.get(id=id)
    if request.method == "POST":
        expense.title = request.POST['title']
        expense.category = request.POST['category']
        expense.amount = request.POST['amount']
        expense.date = request.POST['date']
        expense.save()
        return redirect('/')
    return render(request, 'edit.html', {'expense': expense})

def delete_expense(request, id):
    Expense.objects.get(id=id).delete()
    return redirect('/')
