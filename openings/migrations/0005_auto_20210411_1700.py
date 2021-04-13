# Generated by Django 3.1.7 on 2021-04-11 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openings', '0004_opening_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesTypes',
            fields=[
                ('category_type', models.CharField(default='Sicilian Defense', max_length=200, primary_key=True, serialize=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openings.categories')),
            ],
        ),
        migrations.AddField(
            model_name='opening',
            name='category_type',
            field=models.ForeignKey(default='Sicilian Defense', on_delete=django.db.models.deletion.CASCADE, to='openings.categoriestypes'),
        ),
    ]