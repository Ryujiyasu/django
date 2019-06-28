# Generated by Django 2.2.1 on 2019-06-15 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mt_Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_typoe', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('artist_name', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
                ('price', models.FloatField()),
                ('pricesum', models.FloatField()),
                ('date', models.DateField()),
                ('importdate', models.DateField()),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Mt_Service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mt_aritstname',
            fields=[
                ('artist_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Mt_Service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
