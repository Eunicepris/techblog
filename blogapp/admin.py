 # vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategorieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'description',
        'date_add',
        'statut',
        'image',
    )
    list_filter = (
        'date_add',
        'statut',
        'id',
        'title',
        'description',
        'date_add',
        'statut',
        'image',
    )


class DetailAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'nom_auteur',
        'description',
        'date_add',
        'statut',
        'image',
        'article',
        'categories_id',
    )
    list_filter = (
        'date_add',
        'statut',
        'categories_id',
        'id',
        'title',
        'nom_auteur',
        'description',
        'date_add',
        'statut',
        'image',
        'article',
        'categories_id',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
_register(models.Detail, DetailAdmin)
