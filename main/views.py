import json
from django.shortcuts import render
from functools import wraps
from django.contrib import messages


def index(request):

    return render(request, 'index.html')


def components(request):

    events = [
        {
        "title": '100 €',
        "start": '2023-03-01',
        "end": '2023-03-01',
        "extendedProps": {
            "type": 'payment',
            "id": 1,
            "amount": 100,
            "observations": 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quod.',
            "paid": True,
        },
        },
        {
        "title": '10 €',
        "start": '2023-03-01',
        "end": '2023-03-01',
        "extendedProps": {
            "type": 'payment',
            "id": 10,
            "amount": 100,
            "observations": 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quod.',
            "paid": False,
        },
        },
        {
        "title": 'Fisioterapia',
        "start": '2023-03-04',
        "end": '2023-03-012',
        "extendedProps": {
            "type": 'service',
            "id": 10,
            "amount": 100,
            "observations": 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quod.',
            "paid": False,
        },
        },
        {
        "title": 'Fisioterapia',
        "start": '2023-03-08',
        "end": '2023-03-08'
        },
        {
        "title": '100€',
        "start": '2023-03-09',
        "end": '2023-03-09'
        },
        {
        "title": '100€',
        "start": '2023-03-10',
        "end": '2023-03-10'
        },
        {
        "title": 'Trabajo Social',
        "start": '2023-03-11',
        "end": '2023-03-11'
        },
    ]

    context = {
        'options1': {'1':'1','2':'2','3':'3','4':'4'},
        'options2': {'4':'5','9':'8'},
        'stockTest': {'name':'STOCKINGS','quantity':9999},
        'object_name': 'ejemplo',
        'events_json': json.dumps(events),
    }

    return render(request, 'components.html', context)


def custom_403(request):
    return render(request, 'error/403.html', {}, status=403)

def asem_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if request.user.ong.name.lower() == "asem":
            return function(request, *args, **kwargs)
        else:
            messages.error(request, "Necesitas pertenecer a ASEM para acceder a esos datos")
            return custom_403(request)
    return wrapper

    
def videssur_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if request.user.ong.name.lower() == "videssur":
            return function(request, *args, **kwargs)
        else:
            return custom_403(request)
    return wrapper

