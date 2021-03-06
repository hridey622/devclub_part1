# Generated by Django 3.2 on 2021-04-21 14:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=10)),
                ('isbn', models.IntegerField()),
                ('location', models.CharField(max_length=1000)),
                ('availability', models.IntegerField()),
            ],
        ),
    ]
