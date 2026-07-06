from django.shortcuts import render
from django.http import Http404

from .projects_data import PROJECTS


def home(request):
    return render(request, 'portfolio/home.html')


def project_detail(request, slug):
    project = PROJECTS.get(slug)
    if project is None:
        raise Http404("Project not found")
    return render(request, 'portfolio/project_detail.html', {
        'project': project,
        'slug': slug,
    })
