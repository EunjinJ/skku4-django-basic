from django import forms
from .models import Board, Comment


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._widget_update()

    class Meta:
        model = Comment
        fields = ["content"]

    def _widget_update(self):
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class BoardForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._widget_update()

    class Meta:
        model = Board
        fields = ["title", "content", "author"]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': "제목을 입력해주세요."
                }
            )
        }

    def _widget_update(self):
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'