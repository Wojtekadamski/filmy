from django import forms
from django.core.exceptions import ValidationError

from filmyapp.models import Person, Category, Film, Studio


def check_year(value):
    if value <= 1900:
        raise ValidationError('rok musi być więkrzy niż 2900')


def is_upper(val):
    if val[0].islower():
        raise ValidationError('tytul musi się zaczynać z wielkiej litery')


class MovieForm(forms.Form):
    title = forms.CharField(label='Tytuł', widget=forms.Textarea, validators=[is_upper])
    year = forms.IntegerField(label='Rok', validators=[check_year])


class PersonForm(forms.Form):
    first_name = forms.CharField(label='Imie')
    last_name = forms.CharField(label='Nazwisko')


class MovieFullForm(MovieForm):
    directory = forms.ModelChoiceField(queryset=Person.objects.all(), label="Reżyser")
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), label="Kategoria")


class StudioFullForm(forms.Form):
    name = forms.CharField(label='nazwa')
    city = forms.CharField(label='Miasto')


class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = "__all__"
        labels = {
            'title': 'Tytuł',
            'year': 'Rok'
        }
        widgets = {
            'Category': forms.CheckboxSelectMultiple()
        }


class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        labels = {
            'first_name': 'Imie',
            'last_name': 'Nazwisko'
        }


class StudioModelForm(forms.ModelForm):
    class Meta:
        model = Studio
        fields = "__all__"
        labels = {
            'name': 'nazwa',
            'city': 'miasto'
        }
