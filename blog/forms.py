from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        # 使用するmodelをmodels.pyのPostに指定
        model = Post
        # modelで使う要素を指定
        fields = ('title', 'text',)
