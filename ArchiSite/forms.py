from django import forms
from .models import HousePlans,Portfolio

class HousePlansForm(forms.ModelForm):
    class Meta:
        model = HousePlans
        fields = ('images','location','area','description')

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ('title','image1','image2','image3','image4','location','area','description')