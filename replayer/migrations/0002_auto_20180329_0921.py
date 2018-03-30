# Generated by Django 2.0.3 on 2018-03-29 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('replayer', '0001_initial'),
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trace',
            name='model',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trace_model', to='training.PredModels'),
        ),
        migrations.AddField(
            model_name='event',
            name='trace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trace', to='replayer.Trace'),
        ),
    ]