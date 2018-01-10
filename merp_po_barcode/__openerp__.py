# -*- coding: utf-8 -*-
{
    'name': 'Barcode on PO Printed Form',
    "version": "8.0.1.0.0",
    'author': 'Ventor',
    'website': 'https://ventor.tech/',
    'category': '',
    "sequence": 14,
    'complexity': "easy",
    'category': 'Hidden',
    'description': """
        The current module is adding barcode to Printed Form of PO
        It is used just for demo purposes
        
    """,
    'depends': ["base",'stock'],
    'init_xml': [],
    'data': [
        "views/report_purchaseorder.xml",
    ],
    'demo_xml': [],
    'test': [
    ],
    'qweb' : [
    ],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
