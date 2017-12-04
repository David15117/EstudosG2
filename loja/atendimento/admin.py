# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib import admin
from atendimento.models import *
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Produto)
admin.site.register(Vendas)