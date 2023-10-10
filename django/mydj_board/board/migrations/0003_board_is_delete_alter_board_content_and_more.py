# Generated by Django 4.1 on 2023-10-06 04:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0002_alter_board_content_alter_board_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="is_delete",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="board",
            name="content",
            field=models.TextField(
                validators=[
                    django.core.validators.MinLengthValidator(
                        10, "최소 10글자 이상은 입력해주셔야 합니다."
                    )
                ]
            ),
        ),
        migrations.AlterField(
            model_name="board",
            name="title",
            field=models.CharField(
                max_length=255,
                validators=[
                    django.core.validators.MinLengthValidator(
                        2, "최소 세 글자 이상은 입력해주셔야 합니다."
                    )
                ],
            ),
        ),
    ]
