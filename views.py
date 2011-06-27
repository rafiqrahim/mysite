import datetime
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response

__author__ = 'ruffiQ'

def hello(request):
    return HttpResponse("Hello world\n aa")

def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())

def hours_ahead(request, hour_offset):
    try:
         hour_offset = int(hour_offset)
    except ValueError:
         raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
    return render_to_response('hours_ahead.html', locals())