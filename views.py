from django.http import Http404, HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
    now=datetime.datetime.now()
    return render_to_response('current_datetime.html',{'current_date':now})

                  

def hours_ahead(request,offset):
    try:
        hour_offset=int(offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
    return render_to_response('hours_ahead.html',locals())
