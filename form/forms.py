from django import forms

class StartForm(forms.Form):
    Date=forms.DateTimeField(label="Date And Time",widget=forms.DateInput(format='%d/%m/%Y'),
                            input_formats=('%d/%m/%Y', '%d/%m/%Y %H:%M'),help_text="Format: dd/mm/yyyy HH:mm")

    Basic=forms.BooleanField(label="Basic Checkup",required=False)
    Electrical=forms.BooleanField(label="Electrical Checkup",required=False)
    Mechanical=forms.BooleanField(label="Mechanical Checkup",required=False)
    Installation=forms.BooleanField(label="Installation work",required=False)
    Water=forms.BooleanField(label="Chilled Water System",required=False)

class BasicForm(forms.Form):
    BasicNotes=forms.CharField(label="Basic Checkup Notes",max_length=100,widget=forms.Textarea,required=False)
    

class ElectricalForm(forms.Form):
    ElectricalNotes=forms.CharField(label="Electrical Checkup Notes",max_length=100,widget=forms.Textarea,required=False)

class MechanicalForm(forms.Form):
    MechanicalNotes=forms.CharField(label="Mechanical Checkup Notes",max_length=100,widget=forms.Textarea,required=False)

class InstallationForm(forms.Form):
    InstallationNotes=forms.CharField(label="Installation work Notes",max_length=100,widget=forms.Textarea,required=False)

class WaterForm(forms.Form):
    WaterNotes=forms.CharField(label="Water Notes",max_length=100,widget=forms.Textarea,required=False)

class EndForm(forms.Form):
    Customer=forms.CharField(label="Customer Name",max_length=20)
