from django.shortcuts import render
from .models import stage


def index(request):
    stages = stage.objects.all()
    context = {'rings': stages}
    return render(request, 'ring_template.html', context)
