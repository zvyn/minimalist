from django.conf.urls import url
from django.http import HttpResponse as H

urlpatterns = [
    url(r'', lambda r: H('Hello World')),
]
