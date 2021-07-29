from django import forms

from blog.models import Posting


class PostForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ['title', 'photo']
        labels = {
            'title': '제목',
            'photo': '사진'
        }