from django.shortcuts import render
from django.http import HttpResponse
from formtools.wizard.views import SessionWizardView
from .forms import *

from .models import data

FORMS = [("Start", StartForm),
         ("Basic", BasicForm),
         ("Electrical",ElectricalForm),
         ("Mechanical", MechanicalForm),
         ("Installation", InstallationForm),
         ("Water", WaterForm),
         ("End", EndForm)]

TEMPLATES = "wizard_form.html"

def basicnote(wizard):
    """Return true if user opts to Basic Checkup"""
    
    cleaned_data = wizard.get_cleaned_data_for_step('Start') or {'Basic': 'none'}
    return cleaned_data['Basic']

def Electricalnote(wizard):
    """Return true if user opts to Electrical Checkup"""
    
    cleaned_data = wizard.get_cleaned_data_for_step('Start') or {'Electrical': 'none'}
    return cleaned_data['Electrical']

def Mechanicalnote(wizard):
    """Return true if user opts to Mechanical Checkup"""
    
    cleaned_data = wizard.get_cleaned_data_for_step('Start') or {'Mechanical': 'none'}
    return cleaned_data['Mechanical']


def Installationnote(wizard):
    """Return true if user opts to Installation Work"""
    
    cleaned_data = wizard.get_cleaned_data_for_step('Start') or {'Installation': 'none'}
    return cleaned_data['Installation']


def Waternote(wizard):
    """Return true if user opts to Chilled Water System"""
    
    cleaned_data = wizard.get_cleaned_data_for_step('Start') or {'Water': 'none'}
    return cleaned_data['Water']


class Loadform(SessionWizardView):
    def get_template_names(self):
        return TEMPLATES
    def done(self, form_list, **kwargs):
        new = data()
        form_dict={}
        for form in form_list:
            form_dict.update(form.cleaned_data.items())
        # print(form_dict)
        for field, value in form_dict.items(): 
            setattr(new,field,value)
        new.save()
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })