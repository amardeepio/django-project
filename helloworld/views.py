# Create your views here.

from django.template.loader import get_template
from django.template import Context
from django.http import  HttpResponse
import datetime


def hello(request):
    test= "<html><body ><h1>hello world</h1></body></html>"
    
    
    return HttpResponse(test)

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date':now}))
    
    return HttpResponse(html)


                     
                     