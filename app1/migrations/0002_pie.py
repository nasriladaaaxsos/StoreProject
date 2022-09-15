# Generated by Django 3.2.15 on 2022-09-15 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piename', models.TextField(max_length=255)),
                ('piefilling', models.TextField(max_length=255)),
                ('piecrust', models.TextField(max_length=255)),
                ('voteflag', models.BooleanField(default=False)),
                ('createdby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to='app1.user')),
            ],
        ),
    ]
