# Generated by Django 4.1.7 on 2023-04-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsolving', '0015_alter_question_correct_answer_alter_test_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Ответ 1'), (2, 'Ответ 2'), (3, 'Ответ 3'), (4, 'Ответ 4')], default=5),
            preserve_default=False,
        ),
    ]
