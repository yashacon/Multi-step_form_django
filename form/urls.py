from django.urls import path
from .views import *
urlpatterns = [
    path('',Loadform.as_view(FORMS, 
                            condition_dict={
                                'Basic': basicnote,
                                'Electrical':Electricalnote,
                                'Mechanical':Mechanicalnote,
                                'Installation':Installationnote,
                                'Water':Waternote
                            })),
]