# Generated by Django 4.2 on 2023-09-27 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error_type', models.CharField()),
                ('info', models.TextField()),
                ('data', models.TextField()),
                ('path', models.URLField(blank=True, null=True)),
                ('error_occured_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.CharField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Error',
                'verbose_name_plural': 'Errors',
                'ordering': ('-id',),
            },
        ),
    ]