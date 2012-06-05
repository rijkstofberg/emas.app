from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from emas.app import MessageFactory as _


class IOrderFolder(form.Schema, IImageScaleTraversable):
    """
    Container for orders
    """
    

class OrderFolder(dexterity.Container):
    grok.implements(IOrderFolder)
    

class SampleView(grok.View):
    grok.context(IOrderFolder)
    grok.require('zope2.View')
    
    # grok.name('view')
