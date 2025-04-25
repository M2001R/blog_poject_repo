from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]


    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'style': 'width: 100%; height: 40px;'})
        self.fields['content'].widget.attrs.update({'style': 'width: 100%; height: 150px;'})  # ارتفاع أكبر للمحتوى
