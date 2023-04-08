from django.forms import ModelForm,CharField, Textarea
from .models import Twitter

class TwitterForm(ModelForm):
  content = CharField(
    required = True, 
    label="",
    widget = Textarea(
      attrs={
        'class':'textarea is-success is-medium',
        'placeholder':'Twitter something...',
      }
    ),
  )
  class Meta:
    model = Twitter
    exclude = ('user',)