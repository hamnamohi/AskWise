# Generated by Django 4.2.2 on 2023-06-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('detail', models.TextField()),
                ('tags', models.TextField()),
            ],
        ),
    ]