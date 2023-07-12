from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'show',)
    # ordering = ('id',) #crescente
    ordering = ('-id',) #decrescente
    # list_filter = 'created_date', #cria um filtro
    search_fields = 'id', 'first_name', 'last_name', #add um campo de pesquisa
    list_per_page = 10 #indica a qnt de valor por pag
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name', 'show',#editar sem abri contato
    list_display_links = 'id', 'phone' #add link no imput

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # ordering = ('id',) #crescente
    ordering = ('-id',) #decrescente
    



# Register your models here.