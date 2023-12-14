from django.shortcuts import render, redirect
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from .utils import searchprojects, paginateprojects
from django.contrib import messages


def projects(request):
    projects, search_query = searchprojects(request)
    custom_range, projects = paginateprojects(request, projects, 3)
    return render(request, 'projects/projects.html', {'projects': projects,
        'search_query': search_query, 'custom_range': custom_range})


def project(request, pk):
    projectobj = Project.objects.get(id=pk)
    tags = projectobj.tags.all()
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectobj
        review.owner = request.user.profile
        review.save()

        projectobj.getvotecount

        messages.success(request, 'Your review was successfully submitted!')
        return redirect('project', pk=projectobj.id)

    return render(request, 'projects/single-project.html', {"project": projectobj, 'tags': tags, 'form': form})


@login_required(login_url='login')
def createproject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', ' ').split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def updateproject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', ' ').split()
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')
    context = {'form': form, 'project': project}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def deleteproject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete_template.html', context)



