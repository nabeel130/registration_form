# Generated by Django 3.1.1 on 2020-09-11 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobform',
            name='aadharno',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='jobform',
            name='address',
            field=models.CharField(default=None, max_length=256),
        ),
        migrations.AddField(
            model_name='jobform',
            name='bankaccount',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='jobform',
            name='contactno',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='jobform',
            name='contactno1',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='jobform',
            name='designation',
            field=models.CharField(choices=[('ACCOUNTS', 'ACCOUNTS'), ('IT', 'IT'), ('SALES', 'SALES'), ('CUSTOMER SERVICE', 'CUSTOMER SERVICE'), ('DELIVERY SERVICE', 'DELIVERY SERVICE')], default='IT', max_length=50),
        ),
        migrations.AddField(
            model_name='jobform',
            name='drivingno',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='jobform',
            name='email',
            field=models.EmailField(default='@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobform',
            name='ifsc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobform',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
        migrations.AddField(
            model_name='jobform',
            name='name',
            field=models.CharField(default=None, max_length=256),
        ),
        migrations.AddField(
            model_name='jobform',
            name='remarks',
            field=models.BooleanField(default=True),
        ),
    ]
