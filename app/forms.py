import re

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'steps', 'time_minutes', 'image', 'category']


def validate_username(value):
    if not re.match(r'^[\w.@+-]+$', value):
        raise ValidationError('Имя пользователя может содержать только буквы, цифры и следующие символы: @/./+/-/_.')


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Пароль:',
        validators=[validate_password]
    )
    username = forms.CharField(
        help_text="",
        label='Имя пользователя:',
        validators=[validate_username]
    )

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
