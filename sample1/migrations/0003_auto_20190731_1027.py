# Generated by Django 2.2.2 on 2019-07-31 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample1', '0002_employee_even_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('text', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=6)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
