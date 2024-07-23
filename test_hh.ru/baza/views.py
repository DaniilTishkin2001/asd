from django.shortcuts import render
from baza.models import FIASNode


def show_fias(request):
    return render(request, "baza/index.html", {"fias": FIASNode.objects.all()})