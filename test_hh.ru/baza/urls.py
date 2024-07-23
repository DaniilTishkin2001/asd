from django.urls import path

from baza.views import show_fias

urlpatterns = [
    path('', show_fias, name='index'),

]