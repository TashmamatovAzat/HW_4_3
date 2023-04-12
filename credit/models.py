from django.utils import timezone

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, verbose_name='ФИО клиента')
    citizenship = models.CharField(max_length=20, null=False, default='Кыргызстан', verbose_name='Гражданство')
    birth_year = models.IntegerField(null=False, blank=False, verbose_name='Год рождения')
    work_place = models.CharField(max_length=30, null=True, blank=True, verbose_name='Место работы')
    update_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата последнего обновления")

    class Meta:
        db_table = 'customers'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Account(models.Model):
    number = models.CharField(max_length=16, null=False, blank=False, unique=True, verbose_name="Номер аккаунта, набор из 16 символов")
    account_type = models.IntegerField(default=1, blank=False, verbose_name='Тип аккаунта')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        db_table = 'accounts'
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'

    def __str__(self):
        return f'{self.client.name} - {self.number}'


class Credit(models.Model):
    sum = models.IntegerField(null=False, blank=False, verbose_name='Сумма кредита')
    date = models.DateField(default=timezone.now, verbose_name='Дата получения кредита')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'loans'
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'

    def __str__(self):
        return f'{self.account.client.name} -  {self.sum}'
