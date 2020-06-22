from django.utils.translation import gettext_lazy as _
from .models import *
from django.forms import ModelForm, TextInput, Textarea, DateTimeField, SelectMultiple, FileInput, FileField, ImageField
from django.forms import HiddenInput


class New_Tag(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        labels = {
            #whithout label
            'name': _(''),
        }
        widgets = {
            #I'm sitting 'placeholder' for a 'imput fild': name
            'name': TextInput(attrs={'placeholder': 'Tag name'}),
        }

class New_Item(ModelForm):
    class Meta:
        model = Item
        fields = ['name','place', 'tag', 'image']
        widgets = {
            # I'm sitting 'rows' for a 'textarea fild'
            'place': Textarea(attrs={'rows': '3'}),
            'tag': SelectMultiple(attrs={'class': 'selectpicker form-control'}),
            #'image': FileInput(attrs={'id': 'customFile', 'class': 'custom-file-input'}),
            #'last_update': HiddenInput(),
        }