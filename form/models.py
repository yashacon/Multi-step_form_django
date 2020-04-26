from django.db import models

# Create your models here.
class data(models.Model):
    Date=models.DateTimeField(verbose_name="Date And Time")

    Basic=models.BooleanField(verbose_name="Basic Checkup",blank=True)
    Electrical=models.BooleanField(verbose_name="Electrical Checkup",blank=True)
    Mechanical=models.BooleanField(verbose_name="Mechanical Checkup",blank=True)
    Installation=models.BooleanField(verbose_name="Installation work",blank=True)
    Water=models.BooleanField(verbose_name="Chilled Water System",blank=True)

    BasicNotes=models.CharField(verbose_name="Basic Checkup Notes",max_length=100,blank=True)
    ElectricalNotes=models.CharField(verbose_name="Electrical Checkup Notes",max_length=100,blank=True)
    MechanicalNotes=models.CharField(verbose_name="Mechanical Checkup Notes",max_length=100,blank=True)
    InstallationNotes=models.CharField(verbose_name="Installation work Notes",max_length=100,blank=True)
    WaterNotes=models.CharField(verbose_name="Chilled Water System Notes",max_length=100,blank=True)
    Customer=models.CharField(verbose_name="Customer's Name",max_length=20)
