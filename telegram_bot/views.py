from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def webhook_handler(request):
    """
        Handles the Webhook from Telegram when a user engages with
        @lewistrava_bot.
    """
    return HttpResponse(request.data)
