from django import forms
from .models import Message

class SendMessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('send_to', 'message', 'secret_question', 'secret_answer')
        labels = {
            'send_to': 'To',
            'secret_question': 'Secret Question',
            'secret_answer': 'Secret Answer'
        }
    
    def __init__(self, *args, **kwargs):
        super(SendMessageForm,self).__init__(*args, **kwargs)
        self.fields['secret_question'].empty_label = 'Create a message that only the recipient can only answer'

        