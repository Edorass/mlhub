from django.shortcuts import render, get_object_or_404
from .models import MLproject
from .forms import MLProjectForm
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def project_list(request):
    query = request.GET.get('q')
    sort = request.GET.get('sort')

    projects = MLproject.objects.all()

    if query:
        projects = projects.filter(
            Q(title__icontains=query) | Q(tech_stack__icontains=query)
        )

    if sort == 'newest':
        projects = projects.order_by('-created_at')
    elif sort == 'oldest':
        projects = projects.order_by('created_at')
    elif sort == 'title_asc':
        projects = projects.order_by('title')
    elif sort == 'title_desc':
        projects = projects.order_by('-title')

    return render(request, 'projects/project_list.html', {'projects': projects})


@login_required
def add_project(request):
    if request.method == 'POST':
        form = MLProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = MLProjectForm()
    return render(request, 'projects/add_project.html', {'form': form})
@login_required
def edit_project(request, pk):
    project = get_object_or_404(MLproject, pk=pk)
    if request.method == 'POST':
        form = MLProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = MLProjectForm(instance=project)
    return render(request, 'projects/edit_project.html', {'form': form})

@login_required
def delete_project(request, pk):
    project = get_object_or_404(MLproject, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'projects/delete_confirm.html', {'project': project})

def project_detail(request, pk):
    project = get_object_or_404(MLproject, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('project_list')
    else:
        form = UserCreationForm()
    return render(request, 'projects/register.html', {'form': form})

# Create your views here.
