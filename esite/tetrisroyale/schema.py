import graphene

from graphene_django.types import DjangoObjectType

from .models import Tetrisroyale


class MessdatenType(DjangoObjectType):
    class Meta:
        model = Tetrisroyale

class Query(graphene.AbstractType):
    pass