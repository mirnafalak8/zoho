# Generated by Django 4.2.1 on 2023-07-13 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0005_journalcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalcomment',
            name='journal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='zohoapp.journal'),
        ),
    ]
