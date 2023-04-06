# Generated by Django 4.1.3 on 2023-04-06 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room_Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Type', models.CharField(choices=[('S', 'Single'), ('D', 'Double')], max_length=1)),
                ('Building', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.building')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Number', models.PositiveSmallIntegerField(default=0)),
                ('Price', models.FloatField()),
                ('Room_Type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.room_type')),
            ],
        ),
        migrations.CreateModel(
            name='BlockedDay',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Day', models.DateField()),
                ('Room', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.room')),
            ],
        ),
    ]
