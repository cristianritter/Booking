# Generated by Django 4.0.2 on 2022-02-16 12:43

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_usuario_ativo_usuario_criado_usuario_modificado'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagem',
            field=stdimage.models.StdImageField(default=0, upload_to='usuarios', verbose_name='Imagem'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='privilegios',
            field=models.IntegerField(blank=True, choices=[('USER', 'USER'), ('STAFF', 'STAFF'), ('ADMIN', 'ADMIN')], null=True, verbose_name='privilegios'),
        ),
    ]