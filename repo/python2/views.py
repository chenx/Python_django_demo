# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
  return HttpResponse(
    """Hello, world. You're at the python2 homepage.
    <a href="/python2/admin/">Admin</a>
    <a href="/python2/polls/">Polls</a>
    """)
