# Generated by Django 3.1.4 on 2021-01-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0002_auto_20210106_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='show',
            field=models.CharField(choices=[('Ambassador', 'Chicago'), ('Gershwin', 'Wicked'), ('Majestic', 'The Phantom of the Opera'), ('Schoenfeld', 'Come From Away'), ('Shubert', 'To Kill a Mockingbird')], max_length=200),
        ),
    ]