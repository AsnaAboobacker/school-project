# Generated by Django 5.0.6 on 2024-06-28 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=30)),
                ('s_aadhar', models.CharField(max_length=30)),
                ('s_class', models.CharField(max_length=30)),
                ('s_division', models.CharField(max_length=30)),
                ('s_egrantid', models.CharField(max_length=30)),
                ('s_category', models.CharField(max_length=30)),
                ('s_gender', models.CharField(max_length=30)),
            ],
        ),
    ]