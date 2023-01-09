from django.shortcuts import render
from .models import Project
from .models import Theory


def index(request):
	projects = Project.objects.all()
	theory = Theory.objects.all()
	return render(request, 'portfolio/index.html', {'projects': projects, 'theory': theory})
