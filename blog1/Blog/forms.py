# Summary

# This form:

# Builds a user creation/edit system

# Connects to Django User model

# Lets you assign roles

# Lets you activate/deactivate users

# Handles password securely (via view)

# users/forms.py
from django import forms
from django.contrib.auth.models import User, Group

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        empty_label="Select Role",
        label="Role"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_active', 'group']