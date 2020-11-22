# Generated by Django 3.1.3 on 2020-11-22 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('year', models.IntegerField()),
                ('Studio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produced_by', to='filmyapp.studio', verbose_name='Studio')),
                ('category', models.ManyToManyField(null=True, to='filmyapp.Category')),
                ('directory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='directed_by', to='filmyapp.person')),
                ('screen_play', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='screen_play_by', to='filmyapp.person', verbose_name='Scenarzysta')),
            ],
        ),
    ]