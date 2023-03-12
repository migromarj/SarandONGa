from django.shortcuts import render
from .forms import create_payment_form
from .models import Payment
from django.contrib import messages
#import json

def create_payment(request):
    if request.method == 'POST':
        form = create_payment_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'El formulario presenta errores')
    else:
        form = create_payment_form()
    return render(request, 'payment/payment_form.html', {'form': form})



def payment_list(request):
    context = {
        'objects': Payment.objects.all(),
        #'objects_json': json.dumps(list(Payment.objects.all().values())),
        'objects_name': 'Payment',
        'title': 'Lista de Pagos'
    }
    return render(request, 'payment/payment_list.html', {"context":context })

