from xml.etree import ElementTree

from django import forms
from django.core.exceptions import ValidationError
import requests

from .models import Entrepreneur


ARES_BASE_URL = 'http://wwwinfo.mfcr.cz/cgi-bin/ares/darv_std.cgi?ico='


class EntrepreneurForm(forms.ModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        ico = cleaned_data.get('ico')
        try:
            int(ico)
        except ValueError:
            raise ValidationError({'ico': 'IČO should be an integer'}, code='invalid')

        ico = ico.zfill(8)
        weighted_sum = 0
        for i in range(0, 7):
            weighted_sum += (8-i)*int(ico[i])
        ico_check = (11-(weighted_sum % 11)) % 10
        if ico_check != int(ico[7]):
            raise ValidationError({'ico': 'IČO is in wrong format'}, code='invalid')

        ares_response = requests.get(ARES_BASE_URL + ico)
        tree = ElementTree.fromstring(ares_response.content)
        if int(tree[0][0].text) == 0:
            raise ValidationError({'ico': 'No enterpreneur with given IČO found in ARES'}, code='invalid')

        return cleaned_data

    class Meta:
        model = Entrepreneur
        fields = ('name', 'mail', 'ico')
