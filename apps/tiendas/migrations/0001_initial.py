# Generated by Django 2.1.4 on 2018-12-13 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('numero_venta', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('id_tienda', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=20, unique=True)),
                ('stock', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=15)),
                ('comuna', models.CharField(max_length=15)),
                ('dirección', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('usuario', models.CharField(max_length=12)),
                ('contraseña', models.CharField(max_length=40)),
                ('correo', models.CharField(max_length=60)),
                ('tienda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tiendas.Tienda')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('numero', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('cantidad', models.IntegerField()),
                ('total', models.IntegerField()),
                ('comentario', models.CharField(blank=True, max_length=100, null=True)),
                ('rut_vendedor', models.ForeignKey(blank=True, db_column='rut_vendedor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tiendas.Vendedor')),
            ],
        ),
    ]