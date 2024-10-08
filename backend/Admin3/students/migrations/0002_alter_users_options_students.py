# Generated by Django 5.1.1 on 2024-10-08 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={},
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('student_ref', models.AutoField(default=10000, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.users')),
            ],
            options={
                'db_table': 'Students',
                'managed': False,
            },
        ),
    ]