from django.shortcuts import render
from .views import Index
from django.views.generic import TemplateView

# Create your views here.
class index(TemplateView):
	template_name='inicio/Index.html'

