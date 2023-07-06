from django import forms

from todoapp.models import todoapp


class dateinput(forms.DateInput):
    input_type = "date"
class TodoForm(forms.ModelForm):
    date = forms.DateField(widget=dateinput)
    class Meta:
        model = todoapp
        fields = '__all__'
