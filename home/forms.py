from django.forms import ModelForm, RadioSelect, TextInput, Textarea, EmailInput
from home.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['sender', 'email', 'number', 'message', 'category']
        widgets = {
            'sender': TextInput(attrs={'placeholder': 'Name'}),
            'email': EmailInput(attrs={'placeholder': 'Email'}),
            'number': TextInput(attrs={'placeholder': 'Number'}),
            'message': Textarea(attrs={'placeholder': 'Enter your message', 'rows': 6}),
            'category': RadioSelect(),
        }
