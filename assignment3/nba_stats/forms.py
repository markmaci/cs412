from django import forms
from django.core import validators
from django.contrib.auth.models import User
from .models import UserProfile

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email']

    favorite_team = forms.CharField(max_length=100, required=False, label="Favorite NBA Team")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

STAT_OPTIONS = (
    ('---', '---'),
    ('Reg. Season', 'Regular Season'),
    ('Post Season', 'Post Season'),
)

class PlayerSearchForm(forms.Form):
    player_name = forms.CharField(
        label='',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search a player',
                'class': 'form-control',
                'aria-label': 'Player Name'
            }
        ),
        error_messages={
            'required': 'Please enter a player name.'
        }
    )

class StatsDropdownForm(forms.Form):
    option = forms.ChoiceField(choices=STAT_OPTIONS, label="View Stats By:", required=True, 
                               error_messages={'required': 'Please select an option'})
