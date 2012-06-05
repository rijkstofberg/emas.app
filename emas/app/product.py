from five import grok

from z3c.form import field
from zope import schema

from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.app.textfield.widget import RichTextWidget
from plone.app.z3cform.wysiwyg.widget import WysiwygFieldWidget

from emas.app import MessageFactory as _


class IProduct(form.Schema):
    """
    An orderable product (e.g. a printed text book)
    """
    price = schema.Float(
        title=_(u"Price"),
        description=_("Price in Rands."),
        required=True,
    )


class Product(dexterity.Item):
    grok.implements(IProduct)


class AddForm(dexterity.AddForm):
    grok.name('emas.app.product')

    def updateWidgets(self):
        self.fields['IBasic.description'].widgetFactory = WysiwygFieldWidget
        super(AddForm, self).updateWidgets()


class EditForm(dexterity.EditForm):
    grok.context(IProduct)

    def updateWidgets(self):
        self.fields['IBasic.description'].widgetFactory = WysiwygFieldWidget
        super(EditForm, self).updateWidgets()


class View(dexterity.DisplayForm):
    grok.context(IProduct)
    grok.require('zope2.View')


class SampleView(grok.View):
    grok.context(IProduct)
    grok.require('zope2.View')
    
    # grok.name('view')
