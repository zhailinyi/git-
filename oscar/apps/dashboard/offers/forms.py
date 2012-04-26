from django import forms

from django.db.models.loading import get_model

ConditionalOffer = get_model('offer', 'ConditionalOffer')
Condition = get_model('offer', 'Condition')
Benefit = get_model('offer', 'Benefit')


class MetaDataForm(forms.ModelForm):

    class Meta:
        model = ConditionalOffer
        fields = ('name', 'description', 'start_date', 'end_date',)


class ConditionForm(forms.ModelForm):

    class Meta:
        model = Condition


class BenefitForm(forms.ModelForm):

    class Meta:
        model = Benefit


class PreviewForm(forms.Form):
    pass
