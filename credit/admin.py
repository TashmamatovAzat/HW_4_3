from django.contrib import admin

from .models import Account, Client, Credit

admin.site.register(Client)
admin.site.register(Account)


class CreditAdmin(admin.ModelAdmin):
    list_display = ['account', 'sum', 'date']


admin.site.register(Credit, CreditAdmin)

