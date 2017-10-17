# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print request.session.get("words"), "Hello"
    context = {
        "words":request.session.setdefault("words", [])
    }
    print request.session["words"], "World"
    return render(request, "sesswordsApp/index.html", context)

def add(request):
    words = request.session["words"]
    words.append((
        request.POST["word"],
        request.POST["color"],
        bool(request.POST.get("big"))
    ))
    request.session["words"] = words
    return redirect("/sesswords/")

def clear(request):
    request.session["words"] = []
    return redirect("/sesswords/")