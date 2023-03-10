# Generated by Django 4.1.5 on 2023-01-18 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sekolah', '0002_rename_alamat_sekolah_alamat_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sekolah',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Sekolah'},
        ),
        migrations.RemoveField(
            model_name='sekolah',
            name='Hp',
        ),
        migrations.RemoveField(
            model_name='sekolah',
            name='Jenis_Sekolah',
        ),
        migrations.RemoveField(
            model_name='sekolah',
            name='Web',
        ),
        migrations.AddField(
            model_name='sekolah',
            name='Kabupaten_Kota',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sekolah',
            name='Kecamatan',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sekolah',
            name='NPSN',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='sekolah',
            name='Provinsi',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sekolah',
            name='Status',
            field=models.CharField(choices=[('S', 'Swasta'), ('N', 'Negeri')], default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='sekolah',
            name='Telp',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='sekolah',
            name='create_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sekolah_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sekolah',
            name='Alamat',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sekolah',
            name='Email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterModelTable(
            name='sekolah',
            table='Sekolah',
        ),
    ]
