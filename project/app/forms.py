from django import forms 
from.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ("Category","name","description","rate","image")
class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = category
        fields = ("name","image")

  
     
    
    
