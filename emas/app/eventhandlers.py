import datetime
from zope.component import createObject
from Products.CMFCore.utils import getToolByName


def orderAdded(order, event):
    """ Set the userid
    """
    member = order.restrictedTraverse('@@plone_portal_state').member()
    order.userid = member.getId()
    order.date_ordered = datetime.datetime.now()


def orderItemAdded(item, event):
    """ Calculate the total and set the price at purchase time.
    """
    price = item.price or item.related_item.to_object.price
    item.price = price
    item.total = item.quantity * item.price
