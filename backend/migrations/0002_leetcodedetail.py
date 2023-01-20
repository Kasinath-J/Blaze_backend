# Generated by Django 4.1.5 on 2023-01-19 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeetcodeDetail',
            fields=[
                ('date', models.DateField(auto_now=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='backend.profile')),
                ('no_easy_qns', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('no_medium_qns', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('no_difficult_qns', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('overall_raking', models.PositiveIntegerField(blank=True, null=True)),
                ('no_of_submissions', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('languages', models.JSONField(blank=True, null=True)),
                ('skills_advanced', models.JSONField(blank=True, null=True)),
                ('skills_intermediate', models.JSONField(blank=True, null=True)),
                ('skills_fundamental', models.JSONField(blank=True, null=True)),
                ('contests', models.JSONField(blank=True, null=True)),
                ('badges', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]