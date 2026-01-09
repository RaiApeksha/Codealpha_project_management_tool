from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from projects.models import Project
from comments.models import Comment



@login_required
def create_task(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # permission check
    if request.user not in project.members.all():
        return redirect('project_list')

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        Task.objects.create(
            title=title,
            description=description,
            project=project
        )

        return redirect('project_detail', project_id=project.id)

    return render(request, 'tasks/create_task.html', {
        'project': project
    })

@login_required
def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    project = task.project

    # permission check
    if request.user not in project.members.all():
        return redirect('project_list')

    if request.method == "POST":
        new_status = request.POST.get('status')
        if new_status in ['todo', 'progress', 'done']:
            task.status = new_status
            task.save()

    return redirect('project_detail', project.id)

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    project = task.project

    # Permission check
    if request.user not in project.members.all():
        return redirect('project_list')

    # Handle POST requests
    if request.method == "POST":

        # Assign task
        if 'assigned_to' in request.POST:
            user_id = request.POST.get('assigned_to')
            if user_id:
                task.assigned_to_id = user_id
                task.save()

        #  Add comment
        if 'comment' in request.POST:
            comment_text = request.POST.get('comment')
            if comment_text:
                Comment.objects.create(
                    task=task,
                    user=request.user,
                    text=comment_text
                )

        return redirect('task_detail', task.id)

    members = project.members.all()

    return render(request, 'tasks/task_detail.html', {
        'task': task,
        'members': members,
    })
