from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Student, Portfolio

def index(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio_app/index.html', {'portfolios': portfolios})
class StudentListView(ListView):
    model = Student
    template_name = 'portfolio_app/student_list.html'
    context_object_name = 'students'
class StudentDetailView(DetailView):
    model = Student
    template_name = 'portfolio_app/student_detail.html'
    context_object_name = 'student'
class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio_app/portfolio_detail.html'
    context_object_name = 'portfolio'

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Student
class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'major']
    template_name = 'portfolio_app/student_form.html'
    success_url = reverse_lazy('student-list')
