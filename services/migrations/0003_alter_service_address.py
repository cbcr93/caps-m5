# Generated by Django 4.0.6 on 2022-07-15 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adresses', '0002_rename_complementet_address_complement'),
        ('services', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='adresses.address'),
        ),
    ]