from django.shortcuts import render,redirect
from . import util 
import markdown
from django.http import HttpResponseRedirect
from django.urls import reverse
from random import choice ,random
from django import forms 
from encyclopedia import templates
import secrets
import re
import random


markdowner = markdown.Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    entrypage = util.get_entry(entry)
    return render(request, "encyclopedia/entry.html", {
        "entry": markdowner.convert(entrypage),
        "entryTitle": entry
        })

def search(request):
    entries = util.list_entries()
    felid = request.POST.get('q')
    searchlist = []
    for entry in entries:
        if entry.upper() == felid.upper():
            return render(request, "encyclopedia/entry.html", {
                "entry": markdowner.convert(util.get_entry(entry)),
                "felid": felid
            })
        elif felid.upper() in entry.upper():
            searchlist.append(entry)
        else:
            continue
    return render(request, "encyclopedia/search.html", {
        "entries": searchlist,
        "felid": felid
    })


def random_entry (request):
    entries= util.list_entries()
    rand_entry=random.choice(entries)
    entry = util.get_entry(rand_entry)
    return render(request, "encyclopedia/randomentry.html", {
        "entry": markdowner.convert(entry),
    })

def edit_entry(request,entryTitle):
    entry = util.get_entry(entryTitle)
    if request.method == "GET":
        return render(request, "encyclopedia/editentry.html", {
            "entryTitle":entryTitle,
            "entry" :entry})
    else:
        entry = request.POST['newentry']
        util.save_entry(entryTitle,entry)
        return render(request, "encyclopedia/entry.html", {
            "entryTitle":entry,
            "entry" :markdowner.convert(entry)
        })


def create_entry (request):
    if request.method == "POST":
        title = request.POST['title']
        entry = request.POST['entry']
        if title or entry is not None:
            new_entry = util.save_entry(title,entry) 
            return redirect('index')
    return render (request,"encyclopedia/createentry.html",{

            
    })