from django.shortcuts import render, redirect
from .models import Job
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import Form
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login

# Create your views here.
def home(request):
    categories = Job._meta.get_field('category').choices
    jobs = Job.objects.filter(
        expiry_date__gte=datetime.date.today()
    ).order_by('-posted_at')

    search_term = request.GET.get('search')
    if search_term:
        jobs = jobs.filter(
            Q(title__icontains=search_term) |
            Q(company__icontains=search_term) |
            Q(location__icontains=search_term) |
            Q(description__icontains=search_term)
        )

    return render(request, 'jobs/home.html', {
        'jobs': jobs,
        'categories': categories
    })

def job_detail(request, pk):
    job = Job.objects.get(pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})

@login_required()
def post_job(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Form()
    return render(request, 'jobs/post_job.html', {'form': form})

def category(request, category):
    if request.method == 'GET':
        jobs = Job.objects.filter(category__iexact=category).filter(expiry_date__gte=datetime.date.today()).order_by('-posted_at')
    return render(request, 'jobs/category.html', {'jobs': jobs, 'category': category})

@login_required
def my_jobs(request):
    jobs = Job.objects.filter(posted_by=request.user).order_by('-posted_at')
    return render(request, 'jobs/my_jobs.html', {'jobs': jobs})

def signup(request):
    # simple signup view using default UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created and logged in.')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'jobs/signup.html', {'form': form})