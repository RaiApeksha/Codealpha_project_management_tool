from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project

@login_required
def project_list(request):
    projects = request.user.member_projects.all()
    return render(request, 'projects/project_list.html', {
        'projects': projects
    })


@login_required
def create_project(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')

        project = Project.objects.create(
            name=name,
            description=description,
            owner=request.user
        )
        project.members.add(request.user)

        return redirect('project_list')

    return render(request, 'projects/create_project.html')


@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # permission check
    if request.user not in project.members.all():
        return redirect('project_list')

    return render(request, 'projects/project_detail.html', {
        'project': project
    })
