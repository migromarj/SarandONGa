from django.shortcuts import render
from .forms import CreateNewService
from .models import Service

def service_create(request):
    if request.method == "POST":
        form = CreateNewService(request.POST)
        if form.is_valid():
            form.save()
            return service_list(request)

    form = CreateNewService()
    return render(request, 'service/service_form.html', {"form": form})


def service_list(request):

    context = {
        'objects': Service.objects.all(),
        'objects_name': 'Servicio',
        'title': 'Gestión de servicios',
        'search_text': 'Buscar servicio...',
    }

    return render(request, 'service_list.html', context)
