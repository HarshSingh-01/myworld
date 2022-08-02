from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members
from django.db.models import Q
# Create your views here.

def index(request):
    mymembers = Members.objects.all().order_by('firstname').values()
    context = {
        'mymembers':mymembers, 
        'totalMembers': len(Members.objects.all())
    }
    return render(request, "members.html", context)

def add(request):
    return render(request, "add.html", {})

def addrecord(request):
    firstname = request.POST['first']
    lastname  = request.POST['last']

    member = Members(firstname=firstname, lastname=lastname)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request,id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request,id):
    mymember = Members.objects.get(id=id)
    context = {
        "mymember": mymember
    }
    return render(request, "update.html", context)

def updaterecord(request,id):
    first = request.POST['first']
    last = request.POST['last']

    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()

    return HttpResponseRedirect(reverse('index'))

def template(request):
    mymembers = Members.objects.filter( Q(firstname__startswith="G") | Q(firstname__startswith="A") ).values()
    context = {
        'mymembers': mymembers
    }
    return render(request, "template.html", context)
