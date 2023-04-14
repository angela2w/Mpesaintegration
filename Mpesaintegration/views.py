from django.shortcuts import render
from django_daraja.mpesa import utils
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django_daraja.mpesa.core import MpesaClient
from decouple import config
from datetime import datetime

cl = MpesaClient()
stk_push_callback_url = 'https://api.darajambili.com/express-payment'
bz2_callback_url = 'https://api.darajambili.com/b2c/result'


def oauth_success(request):
    r = cl.auth_token()
    return JsonResponse(r, safe=False)


def Index(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone')
        amount = request.POST.get('amount')
        amount = int(amount)
        account_reference = 'ANGELA'
        transaction_reference = 'STK pusg description'
        callback_urls = stk_push_callback_url
        r = cl.stk_push(phone_number, amount, account_reference, transaction_reference, callback_urls)
        return JsonResponse(r.response_description, safe=False)

    return render(request, 'index.html')
