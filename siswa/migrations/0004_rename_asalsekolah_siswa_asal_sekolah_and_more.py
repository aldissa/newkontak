# Generated by Django 4.1.5 on 2023-01-16 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siswa', '0003_rename_alamat_siswa_alamat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siswa',
            old_name='AsalSekolah',
            new_name='Asal_Sekolah',
        ),
        migrations.RenameField(
            model_name='siswa',
            old_name='JenisKelamin',
            new_name='Jenis_Kelamin',
        ),
        migrations.RenameField(
            model_name='siswa',
            old_name='TanggalLahir',
            new_name='Tanggal_Lahir',
        ),
        migrations.RenameField(
            model_name='siswa',
            old_name='TempatLahir',
            new_name='Tempat_Lahir',
        ),
    ]
