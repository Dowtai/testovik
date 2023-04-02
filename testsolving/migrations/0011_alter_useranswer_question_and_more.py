# Generated by Django 4.1.7 on 2023-03-30 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testsolving', '0010_rename_answer_useranswer_user_answer_delete_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qanswers', to='testsolving.question'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='user_answer',
            field=models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, ' 4')]),
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='testsolving.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='useranswer',
            name='test_result',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tanswers', to='testsolving.testresult'),
            preserve_default=False,
        ),
    ]
