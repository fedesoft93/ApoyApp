# Generated by Django 2.1 on 2018-09-08 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apoyo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('identificacion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Apoyo_Menaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_donacion', models.CharField(choices=[('a', 'alimento'), ('m', 'medicina'), ('e', 'enseres')], default='e', max_length=1)),
                ('descripcion', models.TextField()),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('identificacion', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='Número de Identificación')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img/persona/')),
                ('fecha_hora_inicio', models.DateTimeField()),
                ('fecha_hora_fin', models.DateTimeField()),
                ('latitud', models.CharField(blank=True, max_length=50, null=True)),
                ('longitud', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Apoyo_Monetario',
            fields=[
                ('apoyo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fundacion.Apoyo')),
                ('valor_donacion', models.CharField(max_length=10)),
                ('confirmacion', models.CharField(max_length=100)),
                ('dir_correo', models.EmailField(max_length=254)),
            ],
            bases=('fundacion.apoyo',),
        ),
        migrations.CreateModel(
            name='Apoyo_Voluntario',
            fields=[
                ('apoyo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fundacion.Apoyo')),
                ('direccion', models.CharField(blank=True, max_length=20, null=True)),
                ('tel_fijo', models.CharField(blank=True, max_length=20, null=True)),
                ('tel_movil', models.CharField(blank=True, max_length=20, null=True)),
                ('dir_correo', models.EmailField(max_length=254)),
                ('situacion_laboral', models.CharField(choices=[('e', 'empleado'), ('i', 'independiente'), ('d', 'desempleado')], default='e', max_length=1)),
                ('profesion', models.CharField(blank=True, max_length=255, null=True)),
                ('empresa', models.CharField(blank=True, max_length=255, null=True)),
            ],
            bases=('fundacion.apoyo',),
        ),
        migrations.CreateModel(
            name='Fundacion',
            fields=[
                ('entidad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fundacion.Entidad')),
                ('direccion', models.CharField(max_length=20)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=255, null=True)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('latitud', models.CharField(blank=True, max_length=50, null=True)),
                ('longitud', models.CharField(blank=True, max_length=50, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='img/fundacion/')),
            ],
            bases=('fundacion.entidad',),
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('entidad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fundacion.Entidad')),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('apellido', models.CharField(max_length=20)),
                ('genero', models.CharField(choices=[('m', 'masculino'), ('f', 'femenino'), ('i', 'indefinido')], default='m', max_length=1)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('dir_correo', models.EmailField(max_length=254)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='img/persona/')),
                ('fundacion_ids', models.ManyToManyField(blank=True, null=True, to='fundacion.Fundacion')),
            ],
            bases=('fundacion.entidad',),
        ),
        migrations.AddField(
            model_name='evento',
            name='fundacion_ids',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundacion.Fundacion'),
        ),
        migrations.AddField(
            model_name='apoyo_menaje',
            name='fundacion_ids',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundacion.Fundacion'),
        ),
        migrations.AddField(
            model_name='apoyo',
            name='fundacion_ids',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundacion.Fundacion'),
        ),
    ]
