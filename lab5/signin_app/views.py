from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse

people = []


class person:

    def __init__(self, username, password):
        self.username = username
        self.password = password


    


class NewTaskForm(forms.Form):
    inputName = forms.CharField(label='username')
    inputPassword = forms.CharField(label='password')


def firstname(lst):
    temp=[]
    for obj in lst:
        temp.append(obj.username)
    return temp


def index(request):

    return render (request,"signin_app/index.html", {
        'people':firstname(people)
    }) 


def add(request):

    if request.method == "POST":

        form = NewTaskForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['inputName']
            password = form.cleaned_data['inputPassword']

            p = person(username, password)
            people.append(p)

            return HttpResponseRedirect(reverse("index"))

        else:

            return render(request, "signin_app/signinPage.html", {
                "form": form})

    return render(request, "signin_app/signinPage.html", {
        "form": NewTaskForm()})
