# Generated by Django 4.1.1 on 2022-09-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('artist', models.CharField(blank=True, max_length=100, null=True)),
                ('album', models.CharField(blank=True, max_length=100, null=True)),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('audio_file', models.FileField(upload_to='audio_files/')),
            ],
        ),
    ]
