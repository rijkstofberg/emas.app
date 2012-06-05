import logging
from StringIO import StringIO

import transaction
from zope.interface import directlyProvides, directlyProvidedBy

from Products.ATContentTypes.permission import ModifyConstrainTypes
from Products.ATContentTypes.lib.constraintypes import ENABLED
from plone.app.layout.navigation.interfaces import INavigationRoot

from Products.CMFCore.utils import getToolByName
from Products.CMFCore.permissions import ModifyPortalContent, AddPortalContent
from Products.CMFCore.permissions import DeleteObjects

log = logging.getLogger('emas.app-setuphandlers')

DEFAULT_TYPES = ['Folder', 'Document']

def setupPortalContent(portal):
    folders = [
        {'id': 'orders',
        'type': 'emas.app.orderfolder',
        'title': 'Orders',
        'exclude_from_nav':True,
        'publish': False, 
        },
        {'id': 'products_and_services',
        'type': 'emas.app.productsfolder',
        'title': 'Products and Services',
        'exclude_from_nav':True,
        'publish': True,
        },
    ]

    for folder_dict in folders:
        if not portal.hasObject(folder_dict['id']):
            portal.invokeFactory(type_name=folder_dict['type'],
                id=folder_dict['id'],
                title=folder_dict['title'],
                exclude_from_nav=folder_dict.get('exclude_from_nav', False),
            ) 
            folder = portal._getOb(folder_dict['id'])
            
            if folder_dict.get('publish', False):
                wf = getToolByName(portal, 'portal_workflow')
                wf.doActionFor(folder, 'publish')
                folder.reindexObject()
        else:
            folder = portal._getOb(folder_dict['id'])
        folder.manage_permission(ModifyConstrainTypes, roles=['Manager',])
        

def install(context):
    if context.readDataFile('emas.app-marker.txt') is None:
        return
    site = context.getSite()
    setupPortalContent(site)
