from django.db import models

# Create your models here.
from django.core import validators


class Board(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=255, validators=[
        validators.MinLengthValidator(2, "최소 세 글자 이상은 입력해주셔야 합니다.")
    ])
    author = models.CharField(max_length=255)
    content = models.TextField(validators=[
        validators.MinLengthValidator(10, "최소 10글자 이상은 입력해주셔야 합니다."),
    ])  # Text

    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_active_list(cls):
        return cls.objects.filter(is_delete=False)

    @property
    def is_active(self):
        return not self.is_delete


class Comment(models.Model):
    content = models.CharField(max_length=255)
    board = models.ForeignKey("Board", on_delete=models.SET_NULL,
                              null=True,)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)