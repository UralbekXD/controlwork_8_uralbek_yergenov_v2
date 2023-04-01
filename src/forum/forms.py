from django import forms

from .models import Theme, Reply


class ThemeCreationForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['name', 'text']


class ReplyCreationForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 3,
            })
        }