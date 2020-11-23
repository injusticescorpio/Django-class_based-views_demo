from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from basicapp import models
# Create your views here.

class IndexView(TemplateView):
    template_name='index.html'

class SchoolList(ListView):

    context_object_name='school'
    model=models.School
    template_name='basicapp/school_list.html'
    # basically the ListView creates an context dict of name School in lowercase_list from models.School
    #it lists out all the schools that are in the  school model
    # we can create our own name of context dictionary



class SchoolDetailView(DetailView):

    context_object_name='school_details'
    model=models.School
    template_name='basicapp/school_details.html'

    #it shows all the details of a specific entry in school model database
