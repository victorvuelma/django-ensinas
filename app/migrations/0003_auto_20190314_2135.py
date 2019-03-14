# Generated by Django 2.1.7 on 2019-03-14 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190314_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='instituicao',
            field=models.CharField(default=None, max_length=256, verbose_name='Instituição'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='materia',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.Materia', verbose_name='Matéria'),
        ),
    ]