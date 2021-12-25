from django import forms
from .models import Record

WALK_CHOICES = (
        ('0', '0보 이상'),
        ('1000', '1000보 이상'),
        ('2000', '2000보 이상'),
        ('3000', '3000보 이상'),
        ('4000', '4000보 이상'),
        ('5000', '5000보 이상'),
        ('6000', '6000보 이상'),
        ('7000', '7000보 이상'),
        ('8000', '8000보 이상'),
        ('9000', '9000보 이상'),
        ('10000', '10000보 이상'),
    )

class SearchForm(forms.Form):
    check_values = forms.BooleanField(required=False)

class RecordForm(forms.ModelForm):
    cal = forms.CharField(
        label = "섭취 칼로리",
        required=True,
        widget = forms.TextInput(
            attrs={
                'class' : 'cal'
            }
        )
    )
    walk = forms.ChoiceField(
        label = "걸음 수",
        choices = WALK_CHOICES,
        error_messages={'required' : '걸음 수를 선택해주세요.'}
    )
    hour = forms.CharField(
        label = "운동 시간 (시)",
        required=True,
        widget = forms.TextInput(
            attrs={
                'class' : 'hour'
            }
        )
    )
    min = forms.CharField(
        label = "운동 시간 (분)",
        required=True,
        widget = forms.TextInput(
            attrs={
                'class' : 'min'
            }
        )
    )

    class Meta:
        model = Record
        fields = [
            'cal','walk','hour','min']