# Generated by Django 4.2 on 2023-04-12 08:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16, unique=True, verbose_name='Номер аккаунта, набор из 16 символов')),
                ('account_type', models.IntegerField(default=1, verbose_name='Тип аккаунта')),
            ],
            options={
                'verbose_name': 'Счет',
                'verbose_name_plural': 'Счета',
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='ФИО клиента')),
                ('citizenship', models.CharField(default='Кыргызстан', max_length=20, verbose_name='Гражданство')),
                ('birth_year', models.IntegerField(verbose_name='Год рождения')),
                ('work_place', models.CharField(blank=True, max_length=30, null=True, verbose_name='Место работы')),
                ('update_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего обновления')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.IntegerField(verbose_name='Сумма кредита')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата получения кредита')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credit.account')),
            ],
            options={
                'verbose_name': 'Кредит',
                'verbose_name_plural': 'Кредиты',
                'db_table': 'loans',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credit.client'),
        ),
    ]