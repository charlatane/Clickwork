# Generated by Django 3.2.5 on 2021-08-23 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuestViewApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreelancerModel',
            fields=[
                ('FreelancerId', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.TextField()),
                ('Name', models.TextField()),
                ('City', models.TextField()),
                ('Country', models.TextField()),
                ('EducationalInstitution', models.TextField()),
                ('EducationalQualifications', models.TextField()),
                ('Employment', models.TextField()),
                ('CompanyName', models.TextField()),
                ('Skills', models.TextField()),
                ('CategoryName', models.TextField()),
                ('Email', models.TextField()),
                ('AdditionalContactDetails', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('JobId', models.AutoField(primary_key=True, serialize=False)),
                ('ClientName', models.TextField()),
                ('CompanyName', models.TextField()),
                ('Email', models.TextField()),
                ('City', models.TextField()),
                ('Country', models.TextField()),
                ('Headline', models.TextField()),
                ('Description', models.TextField()),
                ('Skills', models.TextField()),
                ('AdditionalRequirements', models.TextField()),
                ('CategoryName', models.TextField()),
            ],
        ),
    ]
